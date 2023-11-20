from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Player
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from players.models import Player, PlayerMatchPoints

@api_view(['GET'])
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
@api_view(['GET'])
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
@api_view(['POST'])
def create_player(request):
    name = request.data.get('name', None)
    country_id = request.data.get('country_id', None)
    age = request.data.get('age', None)
    image = request.FILES.get('image', None)
    team_id = request.data.get('team_id', None)
    jersey_number = request.data.get('jersey_number', None)
    batting_style = request.data.get('batting_style', None)
    bowling_style = request.data.get('bowling_style', None)
    player_type = request.data.get('player_type', None)
    is_captain = request.data.get('is_captain', None)

    if name is None or country_id is None:
        context = {
            'message': 'name or country_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        player = Player.objects.create(
            name=name,
            country_id=country_id,
            age=age,
            image=image,
            team_id=team_id,
            jersey_number=jersey_number,
            batting_style=batting_style,
            bowling_style=bowling_style,
            player_type=player_type,
            is_captain=is_captain
        )

        context = {
            'message': 'Player created successfully',
            'data': {
                'id': player.id,
                'name': player.name,
                'country_id': player.country_id,
                'age': player.age,
                'team_id': player.team_id,
                'jersey_number': player.jersey_number,
                'batting_style': player.batting_style,
                'bowling_style': player.bowling_style,
                'player_type': player.player_type,
                'is_captain': player.is_captain,
            }
        }

        return Response(context, status=status.HTTP_201_CREATED)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except ValueError:
        context = {
            'message': 'Invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_player(request):
    player_id = request.POST.get('player_id', None)
    name = request.POST.get('name', None)
    country_id = request.POST.get('country_id', None)
    age = request.POST.get('age', None)
    image = request.FILES.get('image', None)
    team_id = request.POST.get('team_id', None)
    jersey_number = request.POST.get('jersey_number', None)
    batting_style = request.POST.get('batting_style', None)
    bowling_style = request.POST.get('bowling_style', None)
    player_type = request.POST.get('player_type', None)
    is_captain = request.POST.get('is_captain', None)

    if player_id is None or name is None or country_id is None:
        context = {
            'message': 'player_id, name, or country_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        player = Player.objects.get(id=player_id)
        player.name = name if name is not None else player.name
        player.country_id = country_id if country_id is not None else player.country_id
        player.age = age if age is not None else player.age
        player.image = image if image is not None else player.image
        player.team_id = team_id if team_id is not None else player.team_id
        player.jersey_number = jersey_number if jersey_number is not None else player.jersey_number
        player.batting_style = batting_style if batting_style is not None else player.batting_style
        player.bowling_style = bowling_style if bowling_style is not None else player.bowling_style
        player.player_type = player_type if player_type is not None else player.player_type
        player.is_captain = is_captain if is_captain is not None else player.is_captain
        player.save()

        context = {
            'message': 'Player updated successfully',
            'data': {
                'name': player.name,
                'country_id': player.country_id,
                'age': player.age,
                'team_id': player.team_id,
                'jersey_number': player.jersey_number,
                'batting_style': player.batting_style,
                'bowling_style': player.bowling_style,
                'player_type': player.player_type,
                'is_captain': player.is_captain,
            }
        }

        return Response(context, status=status.HTTP_200_OK)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except ValueError:
        context = {
            'message': 'Invalid player_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_player(request):
    player_id = request.POST.get('player_id', None)

    if player_id is None:
        context = {
            'message': 'player_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        player = Player.objects.get(id=player_id)
        player.delete()

        context = {
            'message': f'Player {player_id} successfully deleted',
        }
        return Response(context, status=status.HTTP_200_OK)

    except Player.DoesNotExist:
        context = {
            'message': 'Player not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        context = {
            'message': 'Invalid player_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

