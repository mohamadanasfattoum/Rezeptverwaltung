from django.contrib import admin

# Register your models here.
from .models import Zutat, Rezept

admin.site.register(Zutat)
admin.site.register(Rezept)