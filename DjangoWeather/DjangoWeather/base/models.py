from django.contrib.auth.models import AbstractUser
from django.db import models

class AuthUser(AbstractUser):
    # Ajoutez vos champs personnalisés ici
    money = models.CharField(max_length=100, blank=True)
