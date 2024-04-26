from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserMoney


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