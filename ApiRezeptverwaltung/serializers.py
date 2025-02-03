from rest_framework import serializers
from .models import Zutat, Rezept


class RezeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezept
        fields = '__all__'
