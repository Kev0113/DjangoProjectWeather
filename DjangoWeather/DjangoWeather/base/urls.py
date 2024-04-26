"""
URL configuration for DjangoWeather project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls'),),
    path('signup/', AuthView, name='AuthView'),
    path('', Home, name='home'),
    path('game/', Game, name='game'),
    path('wheels/', Wheels, name='wheels'),
    path('logout/', Logout, name='custom_logout'),
    path('ranking/', Ranking, name='ranking'),
    path('rules/', Rules, name='rules'),
    path('play/', Play, name='play'),
]
