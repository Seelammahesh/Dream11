from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Match

def get_match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    match_data = {
        'id': match.id,
        'date': match.date,
        'team1': {
            'id': match.team1.id,
            'name': match.team1.name,
            'country': match.team1.country.name if match.team1.country else None,
            'captain_name': match.team1.captain_name,
            'logo': match.team1.logo.url if match.team1.logo else None,
        },
        'team2': {
            'id': match.team2.id,
            'name': match.team2.name,
            'country': match.team2.country.name if match.team2.country else None,
            'captain_name': match.team2.captain_name,
            'logo': match.team2.logo.url if match.team2.logo else None,
        },
        'venue': match.venue,
    }
    return JsonResponse(match_data)

def get_all_matches(request):
    matches = Match.objects.all()
    match_list = [
        {
            'id': match.id,
            'date': match.date,
            'team1': {
                'id': match.team1.id,
                'name': match.team1.name,
                'country': match.team1.country.name if match.team1.country else None,
                'captain_name': match.team1.captain_name,
                'logo': match.team1.logo.url if match.team1.logo else None,
            },
            'team2': {
                'id': match.team2.id,
                'name': match.team2.name,
                'country': match.team2.country.name if match.team2.country else None,
                'captain_name': match.team2.captain_name,
                'logo': match.team2.logo.url if match.team2.logo else None,
            },
            'venue': match.venue,
        }
        for match in matches
    ]
    return JsonResponse(match_list, safe=False)

