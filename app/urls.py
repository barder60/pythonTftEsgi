from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graphStats/', views.json_example, name='json_example'),
    path('game/', views.game, name='game')

]