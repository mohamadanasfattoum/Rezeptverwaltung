from django.urls import path
from .views import RezeptAPIViews

urlpatterns = [
    path("api/", RezeptAPIViews.as_view())
]
