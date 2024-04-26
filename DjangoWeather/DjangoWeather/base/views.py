import random

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserMoney
from .models import Event
from random import randint
from django.http import JsonResponse


@receiver(post_save, sender=User)
def CreateMoneyUser(sender, instance, created, **kwargs):
    if created:
        UserMoney.objects.create(user=instance, money=100)


@login_required
def Home(request):
    user = UserMoney.objects.get(user=request.user)
    Moneyuser = user.money

    ranking = UserMoney.objects.all().order_by('-money')[:5]
    
    return render(request, 'home.html', {'money': Moneyuser, 'ranking': ranking})

def Ranking(request):
    ranking = UserMoney.objects.all().order_by('-money')
    return render(request, 'ranking.html', {'ranking': ranking})

def Rules(request):
    return render(request, 'rules.html')

def Play(request):
    user = UserMoney.objects.get(user=request.user)
    Moneyuser = user.money

    return render(request, 'play.html',{'money': Moneyuser})

def Wheel(self):
    events = Event.objects.all()
    cumulative_probabilities = [0]
    for event in events:
        cumulative_probabilities.append(cumulative_probabilities[-1] + event.probabilite)

    random_number = random.random()
    selected_event = None
    for i in range(len(cumulative_probabilities) - 1):
        if cumulative_probabilities[i] <= random_number < cumulative_probabilities[i + 1]:
            selected_event = events[i]
            break
    return selected_event
def Wheels(self):
    roulette1 = Wheel(self)
    r1 = {
        'nom' : roulette1.nom,
        'multiplicateur': roulette1.multiplicateur,
        'lancers': roulette1.lancers,
        'probabilite': roulette1.probabilite,
    }
    roulette2 = Wheel(self)
    r2 = {
        'nom': roulette2.nom,
        'multiplicateur': roulette2.multiplicateur,
        'lancers': roulette2.lancers,
        'probabilite': roulette2.probabilite,
    }
    roulette3 = Wheel(self)
    r3 = {
        'nom': roulette3.nom,
        'multiplicateur': roulette3.multiplicateur,
        'lancers': roulette3.lancers,
        'probabilite': roulette3.probabilite,
    }
    event_data = {
        'roulette1': r1,
        'roulette2': r2,
        'roulette3': r3,
    }
    return JsonResponse(event_data)

def Game(request):
    if request.method == 'POST':
        data = request.POST
    return render(request, 'game.html', {'data': data})

def AuthView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form" : form})

def Logout(request):
    logout(request)
    return redirect('/')