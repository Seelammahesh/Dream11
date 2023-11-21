from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Team

@api_view(['POST'])
def create_team(request):
    user_id = request.POST.get('user_id', None)
    name = request.POST.get('name', None)
    country_id = request.POST.get('country_id', None)
    captain_name = request.POST.get('captain_name', None)
    logo = request.FILES.get('logo', None)

    if user_id is None or name is None or country_id is None:
        context = {
            'message': 'user_id, name, or country_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        team = Team.objects.create(
            user_id=user_id,
            name=name,
            country_id=country_id,
            captain_name=captain_name,
            logo=logo,
        )

        data = {
            'message': 'Team created successfully',
            'data': {
                'id': team.id,
                'user_id': team.user_id,
                'name': team.name,
                'country_id': team.country_id,
                'captain_name': team.captain_name,
                'logo': team.logo.url if team.logo else None,
            }
        }

        return Response(data, status=status.HTTP_201_CREATED)

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
def update_team(request):
    team_id = request.POST.get('team_id', None)

    if team_id is None:
        context = {
            'message': 'team_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        team = Team.objects.get(id=team_id)
    except Team.DoesNotExist:
        context = {
            'message': 'Team not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    name = request.POST.get('name', team.name)
    country_id = request.POST.get('country_id', team.country_id)
    captain_name = request.POST.get('captain_name', team.captain_name)
    logo = request.FILES.get('logo', team.logo)

    try:
        team.name = name
        team.country_id = country_id
        team.captain_name = captain_name
        team.logo = logo
        team.save()

        data = {
            'message': 'Team updated successfully',
            'data': {
                'id': team.id,
                'user_id': team.user_id,
                'name': team.name,
                'country_id': team.country_id,
                'captain_name': team.captain_name,
                'logo': team.logo.url if team.logo else None,
            }
        }

        return Response(data, status=status.HTTP_200_OK)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_team(request):
    team_id = request.POST.get('team_id', None)

    if team_id is None:
        context = {
            'message': 'team_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        team = Team.objects.get(id=team_id)
        team.delete()

        context = {
            'message': f'Team {team_id} successfully deleted',
        }
        return Response(context, status=status.HTTP_200_OK)

    except Team.DoesNotExist:
        context = {
            'message': 'Team not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        context = {
            'message': 'Invalid team_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team_data = {
        'id': team.id,
        'name': team.name,
        'country': team.country.name if team.country else None,
        'captain_name': team.captain_name,
        'logo': team.logo.url if team.logo else None,
    }
    return Response(team_data)
@api_view(['GET'])
def get_all_teams(request):
    teams = Team.objects.all()
    team_list = [
        {
            'id': team.id,
            'name': team.name,
            'country': team.country.name if team.country else None,
            'captain_name': team.captain_name,
            'logo': team.logo.url if team.logo else None,
        }
        for team in teams
    ]
    return Response(team_list)
