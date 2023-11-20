from django.urls import path
from .views import get_player,get_all_players,update_player,delete_player,create_player

urlpatterns = [
    path('players/<int:player_id>/', get_player, name='get_player'),
    path('players/', get_all_players, name='get_all_players'),
path('update_player/<int:player_id>/', update_player, name='update_player'),
    path('delete_player/<int:player_id>/', delete_player, name='delete_player'),
    path('create_player/', create_player, name='create_player'),
]