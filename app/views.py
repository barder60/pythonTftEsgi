import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .services.championsService import addSelectedChampions, can_add_selected_champion, get_selected_champion, \
    reset_champion_remaining
import os

from app.utils.ChampionUtils import parseChampionJson, get_starting_stock_of_cost
from .utils.ChampionUtils import updateAllSelectedChamp

champions = parseChampionJson(os.getcwd() + '/ressources/champions.json')
selected_champions = []
champions_bought_by_cost = [0, 0, 0, 0, 0]


def index(request):
    return render(request, 'app/index.html')


def game(request):
    global selected_champions
    print(selected_champions)

    context = {
        'champion_list' : champions,
        'selectedChampions' : selected_champions,
        'championsBoughtByCost' : champions_bought_by_cost
    }
    return render(request, 'app/game.html', context)


def new_selected_champion(request):
    global selected_champions
    name = request.GET.get('name')

    if not can_add_selected_champion(selected_champions, name):
        return JsonResponse({}, status=401)


    for champ in champions :
        if name == champ.name :
            addSelectedChampions(selected_champions, champ)

    updateAllSelectedChamp(selected_champions, 4, champions_bought_by_cost)
    inserted_champion = [x for x in selected_champions if x.name == name]
    return JsonResponse({"inserted_champion": json.dumps(inserted_champion[0].__dict__)}, status=200)


def remove_selected_champion(request):
    global selected_champions
    global champions_bought_by_cost
    name = request.GET.get('name')
    reset = request.GET.get('reset')
    champion_to_remove = get_selected_champion(selected_champions, name)

    if reset:
        champions_bought_by_cost = reset_champion_remaining(champions_bought_by_cost, champion_to_remove)
    selected_champions = [x for x in selected_champions if x != champion_to_remove]
    updateAllSelectedChamp(selected_champions, 4, champions_bought_by_cost)
    return JsonResponse({'cost': champion_to_remove.cost, 'value': str(champions_bought_by_cost[champion_to_remove.cost - 1])}, status=200)


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
    updateAllSelectedChamp(selected_champions, 4, champions_bought_by_cost)
    return JsonResponse({'cost': resource[2], 'value': str(champions_bought_by_cost[int(resource[2]) - 1])}, status=200)

def champion_in_team_update(request):
    global selected_champions
    resource = request.GET.get('name')
    resource = resource.split('-')

    if len(resource) == 3:
        champion = next((champion for champion in selected_champions if champion.name == resource[2]), None)
        if champion is not None:
            if resource[0] == 'inc':
                if get_starting_stock_of_cost(champion.cost) - champion.playerCount - champion.otherCount > 0:
                    champion.playerCount += 1
                else:
                    return HttpResponse("", status=416)
            elif resource[0] == 'dec':
                if champion.playerCount != 0:
                    champion.playerCount -= 1
                else:
                    return HttpResponse("", status=416)

    updateAllSelectedChamp(selected_champions, 4, champions_bought_by_cost)
    return JsonResponse({'name': resource[2], 'value': champion.playerCount}, status=200)

def champion_in_enemies_update(request):
    global selected_champions

    resource = request.GET.get('name')
    resource = resource.split('-')
    if len(resource) == 3:
        champion = next((champion for champion in selected_champions if champion.name == resource[2]), None)
        if champion is not None:
            if resource[0] == 'inc':
                if get_starting_stock_of_cost(champion.cost) - champion.playerCount - champion.otherCount > 0:
                    champion.otherCount += 1
                else:
                    return HttpResponse("", status=416)
            elif resource[0] == 'dec':
                if champion.otherCount != 0:
                    champion.otherCount -= 1
                else:
                    return HttpResponse("", status=416)
    updateAllSelectedChamp(selected_champions, 4, champions_bought_by_cost)
    return JsonResponse({'name': resource[2], 'value': champion.otherCount}, status=200)

def get_selected_champ(request):
    global selected_champions
    allSelectedChampJson = []
    for champions in selected_champions:
        allSelectedChampJson.append(champions.__dict__)
    return JsonResponse({"selected_champions":allSelectedChampJson}, status=200)

def json_example(request):
    context = {"categories": [75,25,0,0,0]}
    return render(request, 'app/graphStats.html', context=context)


