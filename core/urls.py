from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),  # Beispiel: Standard-View für die Core-App
    path('dashboard/', views.dashboard, name='dashboard'),  # Beispiel: Standard-View für die Core-App
    
]
