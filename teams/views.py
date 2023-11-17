from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Team

def get_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team_data = {
        'id': team.id,
        'name': team.name,
        'country': team.country.name if team.country else None,
        'captain_name': team.captain_name,
        'logo': team.logo.url if team.logo else None,
    }
    return JsonResponse(team_data)

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
    return JsonResponse(team_list, safe=False)
