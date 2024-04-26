from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User

# Create your models here.
class UserMoney(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=100)
    
class Event(models.Model):
    nom = models.CharField(max_length=100)
    multiplicateur = models.FloatField()
    lancers = models.IntegerField()
    probabilite = models.FloatField()
    def __str__(self):
        return self.nom