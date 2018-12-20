from django.shortcuts import render
from .models import Evento

def home(request):
    e = Evento.objects.all()
    return render(request, 'home.html', {'evento': e})