from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import LeaderboardEntry

def get_leaderboard_entry(request, entry_id):
    entry = get_object_or_404(LeaderboardEntry, id=entry_id)
    entry_data = {
        'id': entry.id,
        'user': {
            'id': entry.user.id,
            'username': entry.user.username,
            'email': entry.user.email,

        },
        'points': entry.points,
    }
    return JsonResponse(entry_data)

def get_all_leaderboard_entries(request):
    entries = LeaderboardEntry.objects.all()
    entry_list = [
        {
            'id': entry.id,
            'user': {
                'id': entry.user.id,
                'username': entry.user.username,
                'email': entry.user.email,

            },
            'points': entry.points,
        }
        for entry in entries
    ]
    return JsonResponse(entry_list, safe=False)

