import json
from ..project_models.champion import Champion
from easydict import EasyDict as edict
from .fileManager import FileManager


def parseChampionJson(path):
    data = FileManager()

    champions = []
    with open(path, "r") as file:
        json_champions = json.load(file)

        for json_champion in json_champions:
            championName = json_champion['name'].lower()
            championName = championName.replace(" ", "")
            championName = championName.replace("'", "")
            champion = Champion(json_champion['name'], json_champion['cost'], json_champion['traits'],data['png'][championName])
            champions.append(champion)

    return champions


def get_starting_stock_of_cost(cost):
    data = edict(FileManager())
    with open(data.json.rules, "r") as json_file:
        data_rules = json.load(json_file)
        champ_counter_list = edict(data_rules)
        # TODO : prevoir erreur de retour pour raison inconnu
        return champ_counter_list.champCounter[cost - 1]
