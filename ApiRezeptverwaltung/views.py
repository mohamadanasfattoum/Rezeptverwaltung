from django.shortcuts import render

from rest_framework import generics
from .models import Zutat, Rezept
from .serializers import RezeptSerializer


class RezeptAPIViews(generics.ListCreateAPIView):
    queryset = Rezept
    serializer_class = RezeptSerializer