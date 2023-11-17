from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Player

def get_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    player_data = {
        'id': player.id,
        'name': player.name,
        'team': player.team.name if player.team else None,
        'position': player.position,
        'jersey_number': player.jersey_number,
    }
    return JsonResponse(player_data)

def get_all_players(request):
    players = Player.objects.all()
    player_list = [
        {
            'id': player.id,
            'name': player.name,
            'team': player.team.name if player.team else None,
            'position': player.position,
            'jersey_number': player.jersey_number,
        }
        for player in players
    ]
    return JsonResponse(player_list, safe=False)

