from django.contrib import admin
from base.models import *

# Register your models here.
@admin.register( Event )
class Event (admin. ModelAdmin ):
    list_display = ('id', 'nom', 'multiplicateur', 'probabilite', 'lancers')