import os

from django.shortcuts import render
from django.http import HttpResponse

from .project_models.champion import Champion
from .services.championsService import addSelectedChampions
# Create your views here.
from django.template import loader
from .project_models import champion
from .utils.ChampionUtils import parseChampionJson
# Create your views here.
import os

from app.utils.ChampionUtils import parseChampionJson

champions = parseChampionJson(os.getcwd() + '/ressources/champions.json')
selected_champions = []
champions_bought_by_cost = [0, 0, 0, 0, 0]


def index(request):
    return render(request, 'app/index.html')


def game(request):
    global selected_champions

    for champ in champions :
        if champ.name == 'Ahri' :
            selected_champions = addSelectedChampions(selected_champions, champ)

    context = {
        'champion_list' : champions,
        'selectedChampions' : selected_champions,
        'championsBoughtByCost' : champions_bought_by_cost
    }
    return render(request, 'app/game.html', context)


def json_example(request):
    context = {"categories": [75,25,0,0,0]}
    return render(request, 'app/graphStats.html', context=context);
