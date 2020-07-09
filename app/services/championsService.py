from app.project_models.selectedChampion import SelectedChampion


def addSelectedChampions(selectedChampions, champion):
    selectedChampion = SelectedChampion(champion.name, champion.cost, champion.traits, champion.pngPath)
    selectedChampions.append(selectedChampion)

    return selectedChampions
