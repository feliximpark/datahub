from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),  # Beispiel: Standard-View für die Core-App
   
]