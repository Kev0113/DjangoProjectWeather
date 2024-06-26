from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User

# Create your models here.
class UserMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.FloatField(default=100)
    
class Event(models.Model):
    nom = models.CharField(max_length=100)
    multiplicateur = models.FloatField(default=0)
    multiplicateur_two = models.FloatField(default=0)
    multiplicateur_three = models.FloatField(default=0)
    lancers = models.IntegerField(default=0)
    lancers_two = models.IntegerField(default=0)
    lancers_three = models.IntegerField(default=0)
    probabilite = models.FloatField()
    def __str__(self):
        return self.nom