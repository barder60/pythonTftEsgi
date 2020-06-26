import os

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.template import loader
from .project_models import champion

from app.utils.ChampionUtils import parseChampionJson


def index(request):
    return render(request, 'app/index.html')

def game(request):
    champions = parseChampionJson(os.getcwd() + '/ressources/champions.json')
    selectedChampions = []
    championsBoughtByCost = [0, 0, 0, 0, 0]
    context = {
        'champion_list' : champions,
        'selectedChampions' : selectedChampions,
        'championsBoughtByCost' : championsBoughtByCost
    }
    return render(request, 'app/game.html', context)

def json_example(request):
    context = {"categories": [75,25,0,0,0]}
    return render(request, 'app/graphStats.html', context=context)