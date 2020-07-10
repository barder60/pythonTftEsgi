from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/GetselectedChamp', views.get_selected_champ, name="get_selected_champ"),
    path('game/level/update', views.update_level, name="update_level"),
    path('game/championInEnemies/update', views.champion_in_enemies_update, name='champion_in_enemies_update'),
    path('game/championInTeam/update', views.champion_in_team_update, name='champion_in_team_update'),
    path('game/championsByCost/update', views.update_champion_bought, name='update_champion_bought'),
    path('game/selectedChamp/add', views.new_selected_champion, name='new_selected_champion'),
    path('game/selectedChamp/delete', views.remove_selected_champion, name='remove_selected_champion'),
    path('graphStats/', views.json_example, name='json_example'),
    path('game/', views.game, name='game'),
]