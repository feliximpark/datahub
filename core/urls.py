from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Beispiel: Standard-View für die Core-App
]
