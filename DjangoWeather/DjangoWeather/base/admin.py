from django.contrib import admin
from base.models import *
from django.contrib.auth.models import AbstractUser, Group, Permission, User


# Register your models here.
@admin.register( UserMoney )
class MoneyUserAdmin(admin.ModelAdmin):

    list_display = ('Username', 'money')

    def Username(self, obj):
        utilisateur = User.objects.get(id=obj.user_id)
        return utilisateur.username
