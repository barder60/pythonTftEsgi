import os

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .services.championsService import addSelectedChampions
import os

from app.utils.ChampionUtils import parseChampionJson, get_starting_stock_of_cost

champions = parseChampionJson(os.getcwd() + '/ressources/champions.json')
selected_champions = []
champions_bought_by_cost = [0, 0, 0, 0, 0]


def index(request):
    return render(request, 'app/index.html')


def game(request):
    global selected_champions



    context = {
        'champion_list' : champions,
        'selectedChampions' : selected_champions,
        'championsBoughtByCost' : champions_bought_by_cost
    }
    return render(request, 'app/game.html', context)

def new_selected_champion(request):
    global selected_champions
    name = request.GET.get('name')
    for champ in champions :
        if name == champ.name :
            selected_champions = addSelectedChampions(selected_champions, champ)
    context = {
        'champion_list': champions,
        'selectedChampions': selected_champions,
        'championsBoughtByCost': champions_bought_by_cost
    }
    return render(request, 'app/game.html', context)


def update_champion_bought(request):
    global champions_bought_by_cost
    resource = request.GET.get('name')
    resource = resource.split('-')

    if len(resource) == 3:
        if resource[0] == 'inc':
            champions_bought_by_cost[int(resource[2]) - 1] = champions_bought_by_cost[ int(resource[2]) - 1] + 1
            starting_cost = get_starting_stock_of_cost(int(resource[2]))
            if champions_bought_by_cost[int(resource[2]) - 1] > starting_cost:
                champions_bought_by_cost[int(resource[2]) - 1] = starting_cost
                return HttpResponse("La limite est de " + str(starting_cost) + " pour ce coût", status=416)
        elif resource[0] == 'dec':
            champions_bought_by_cost[int(resource[2]) - 1] = champions_bought_by_cost[int(resource[2]) - 1] - 1
            if champions_bought_by_cost[int(resource[2]) - 1] < 0:
                champions_bought_by_cost[int(resource[2]) - 1] = 0
                return HttpResponse("", status=416)

    return JsonResponse({'cost': resource[2], 'value': str(champions_bought_by_cost[int(resource[2]) - 1])}, status=200)


def json_example(request):
    context = {"categories": [75,25,0,0,0]}
    return render(request, 'app/graphStats.html', context=context)
