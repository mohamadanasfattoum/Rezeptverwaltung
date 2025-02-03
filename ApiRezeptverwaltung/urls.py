from django.urls import path
from .views import RezeptAPIViews

urlpatterns = [
    path("rezepte/", RezeptAPIViews.as_view())
]
