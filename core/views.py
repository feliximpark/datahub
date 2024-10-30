
from django.shortcuts import render

def home(request):
    return render(request, 'core/0_base.html')