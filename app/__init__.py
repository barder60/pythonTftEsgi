from .utils.fileManager import datafileManagerTft
from .utils.ChampionUtils import parseChampionJson
import os
from easydict import EasyDict as edict
# fileManager = datafileManagerTft()
# fileManager = edict(fileManager)
parseChampionJson(os.getcwd() + '/ressources/champions.json')