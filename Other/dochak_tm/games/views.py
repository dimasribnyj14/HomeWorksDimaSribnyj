from django.shortcuts import render
from games.models import *
# Create your views here.
def show_release_year_page(request):
    list_years = Release_Year.objects.all()
    return render(request,'release_years.html',context={'list_years':list_years})
def show_main_page(request,games_pk=id):
    list_games = Game.objects.filter(id=games_pk)
    return render(request,'main.html',context={'list_games':list_games})
