from django.shortcuts import render
from django.http import HttpResponse
from .project_models import champion
from .utils.ChampionUtils import parseChampionJson
# Create your views here.
import os

def index(request):
    return render(request, 'app/index.html')

def json_example(request):
    #test = parseChampionJson(os.getcwd() + '/ressources/champions.json')
    #for item in test:
     #   print(item)
    context = {"categories": [75,25,0,0,0]}
    return render(request, 'app/graphStats.html', context=context)