from app.project_models.champion import Champion
from ..utils.fileManager import FileManager
from easydict import EasyDict as edict
import json
class SelectedChampion(Champion):
    def __init__(self, name, cost, traits, pngPath):
        Champion.__init__(self,name, cost, traits, pngPath)
        self.playerCount = 0
        self.otherCount = 0
        self.dropRateOfAll = 0
        self.dropRateOfSameCost = 0

    def __str__(self):
        return self.name + " obtenue= " + str(self.playerCount) + " adverse= " + str(self.otherCount)

    def updateDropRate(self, playerLevel, stockSameCostRemaining):
        # stockSameCostRemaining => le nombre de perso du meme cout restant
        # stockAllRemaining => le nombre de perso restant

        # TODO costDropRate => récuperer le pourcentage d'obtenir les heros du cout => self.cost
        # TODO avoir le stock de départ du personnage
        startingStock = self.getStartingStock(self)
        costDropRate = self.getCostDropRate(self, playerLevel)


        selectedChampionRemaining = startingStock - (self.otherCount + self.playerCount)
        self.dropRateOfSameCost = selectedChampionRemaining * 100 / stockSameCostRemaining
        self.dropRateOfAll = self.dropRateOfSameCost * costDropRate

    def getStartingStock(self):
        data = edict(FileManager())
        with open(data.json.rules, "r") as json_file:
            dataRules = json.load(json_file)
            champCounterList = edict(dataRules)
            # TODO : prevoir erreur de retour pour raison inconnu
            return champCounterList.champCounter[self.cost - 1]

    def getCostDropRate(self, playerLevel):
        data = edict(FileManager())

        with open(data.json.rules, "r") as json_file:
            dataRules = json.load(json_file)
            champCounterList = edict(dataRules)
            costDropArray = champCounterList.statsByLevel[playerLevel - 1].stats
            return costDropArray[self.cost - 1]
