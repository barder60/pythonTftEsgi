from app.project_models.champion import Champion


class SelectedChampion(Champion):
    def __init__(self, name, cost, traits, pngPath):
        Champion.__init__(name, cost, traits, pngPath)
        self.playerCount = 0
        self.otherCount = 0
        self.dropRateOfAll = 0
        self.dropRateOfSameCost = 0

    def updateDropRate(self, playerLevel, stockSameCostRemaining):
        # stockSameCostRemaining => le nombre de perso du meme cout restant
        # stockAllRemaining => le nombre de perso restant

        # TODO costDropRate => récuperer le pourcentage d'obtenir les heros du cout => self.cost
        # TODO avoir le stock de départ du personnage
        startingStock = 15
        costDropRate = 25


        selectedChampionRemaining = startingStock - (self.otherCount + self.playerCount)
        self.dropRateOfSameCost = selectedChampionRemaining * 100 / stockSameCostRemaining
        self.dropRateOfAll = self.dropRateOfSameCost * costDropRate
