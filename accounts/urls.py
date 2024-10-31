from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='index'),  # Beispiel: Standard-View für die Core-App
   
    path('register/', views.register, name='register'),  # Beispiel: Standard-View für die Core-App
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
  
]