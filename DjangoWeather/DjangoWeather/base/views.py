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


@receiver(post_save, sender=User)
def CreateMoneyUser(sender, instance, created, **kwargs):
    if created:
        UserMoney.objects.create(user=instance, money=100)


@login_required
def Home(request):
    return render(request, 'home.html')

def Wheel():
    print('Wheel')

def Game(request):
    Wheel()
    events = Event.objects.all()
    event = Event.objects.get(id=1)
    return render(request, 'game.html', {'events': events})

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