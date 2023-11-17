from django.urls import path
from .views import get_player,get_all_players

urlpatterns = [
    path('players/<int:player_id>/', get_player, name='get_player'),
    path('players/', get_all_players, name='get_all_players'),
]