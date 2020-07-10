from .utils.fileManager import datafileManagerTft
from .utils.ChampionUtils import parseChampionJson
from .project_models.selectedChampion import SelectedChampion
import os
from easydict import EasyDict as edict
# fileManager = datafileManagerTft()
# fileManager = edict(fileManager)
champions = parseChampionJson(os.getcwd() + '/ressources/champions.json')
