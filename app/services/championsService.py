from app.project_models.selectedChampion import SelectedChampion


def addSelectedChampions(selectedChampions, champion):
    print(champion.name)
    print(champion.traits)
    print(champion.cost)
    print(champion.pngPath)
    selectedChampion = SelectedChampion(champion.name, champion.cost, champion.traits, champion.pngPath)
    selectedChampions.append(selectedChampion)

    return selectedChampions
