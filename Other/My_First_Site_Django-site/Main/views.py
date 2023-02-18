from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'Main/index.html', {'title':'SilverCoinStudios','tasks':tasks})

def games(request):
    return render(request, 'Main/games.html')

def about(request):
    return render(request, 'Main/about-us.html')