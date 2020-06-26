from .utils.fileManager import datafileManagerTft
from .utils.ChampionUtils import parseChampionJson
from .project_models.selectedChampion import SelectedChampion
import os

result = parseChampionJson(os.getcwd() + '/ressources/champions.json')

print(SelectedChampion.getStartingStock(result[0]))
print(SelectedChampion.getCostDropRate(result[0]))