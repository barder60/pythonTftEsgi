from app.project_models.selectedChampion import SelectedChampion


def addSelectedChampions(selectedChampions, champion):
    selectedChampion = SelectedChampion(champion.name, champion.cost, champion.traits, champion.pngPath)
    selectedChampions.append(selectedChampion)

    return selectedChampions


def can_add_selected_champion(selected_champions, name):
    if len([x for x in selected_champions if x.name == name]) > 0:
        return False
    if len(selected_champions) > 8:
        return False

    return True


def get_selected_champion(selected_champions, name):
    return [x for x in selected_champions if x.name == name][0]


def reset_champion_remaining(champion_by_cost, selected_champion: SelectedChampion):
    cost = selected_champion.cost
    champion_by_cost[cost-1] = champion_by_cost[cost-1] - selected_champion.playerCount
    if champion_by_cost[cost - 1] < 0:
        champion_by_cost[cost - 1] = 0
    return champion_by_cost


