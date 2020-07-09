from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/championsByCost/update', views.update_champion_bought, name='update_champion_bought'),
    path('game/selectedChamp/add', views.new_selected_champion, name='new_selected_champion'),
    path('game/selectedChamp/delete', views.remove_selected_champion, name='remove_selected_champion'),
    path('graphStats/', views.json_example, name='json_example'),
    path('game/', views.game, name='game'),
]