from rest_framework import serializers
from .models import Zutat, Rezept


class ZutatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zutat
        fields = ['name','menge','einheit']


class RezeptSerializer(serializers.ModelSerializer):
    zutaten = ZutatSerializer(many = True)
    class Meta:
        model = Rezept
        fields = '__all__'
