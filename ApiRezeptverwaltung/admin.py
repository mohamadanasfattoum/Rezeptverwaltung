from django.contrib import admin

# Register your models here.
from .models import Zutat, Rezept


class RezeptAdmin(admin.ModelAdmin):
    filter_horizontal = ('zutaten',)


admin.site.register(Zutat)
admin.site.register(Rezept,RezeptAdmin)