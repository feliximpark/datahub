
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    # Prüfen, ob der Benutzer eingeloggt ist
    if request.user.is_authenticated:
        # Eingeloggte Benutzer werden auf eine spezielle Startseite weitergeleitet
        return redirect('dashboard')  # 'dashboard' ist der Name der URL für die neue Startseite

    # Nicht eingeloggte Benutzer sehen die allgemeine Startseite
    return render(request, 'core/home_base.html')

@login_required
def dashboard(request):
    # Die Startseite für eingeloggte Benutzer
    return render(request, 'core/dashboard.html')
