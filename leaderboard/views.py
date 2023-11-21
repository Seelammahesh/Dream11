from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import LeaderboardEntry
from users.models import CustomUser

@api_view(['POST'])
def create_leaderboard_entry(request):
    user_id = request.POST.get('user_id', None)
    points = request.POST.get('points', None)

    if user_id is None or points is None:
        context = {
            'message': 'user_id or points is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(id=user_id)

        leaderboard_entry = LeaderboardEntry.objects.create(
            user=user,
            points=points,
        )

        data = {
            'message': 'LeaderboardEntry created successfully',
            'data': {
                'id': leaderboard_entry.id,
                'user_id': leaderboard_entry.user_id,
                'points': leaderboard_entry.points,
            }
        }

        return Response(data, status=status.HTTP_201_CREATED)

    except CustomUser.DoesNotExist:
        context = {
            'message': 'Invalid user_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_leaderboard_entry(request):
    leaderboard_entry_id = request.POST.get('leaderboard_entry_id', None)

    if leaderboard_entry_id is None:
        context = {
            'message': 'leaderboard_entry_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        leaderboard_entry = LeaderboardEntry.objects.get(id=leaderboard_entry_id)
    except LeaderboardEntry.DoesNotExist:
        context = {
            'message': 'LeaderboardEntry not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    user_id = request.POST.get('user_id', leaderboard_entry.user_id)
    points = request.POST.get('points', leaderboard_entry.points)

    try:
        user = CustomUser.objects.get(id=user_id)

        leaderboard_entry.user = user
        leaderboard_entry.points = points
        leaderboard_entry.save()

        data = {
            'message': 'LeaderboardEntry updated successfully',
            'data': {
                'id': leaderboard_entry.id,
                'user_id': leaderboard_entry.user_id,
                'points': leaderboard_entry.points,
            }
        }

        return Response(data, status=status.HTTP_200_OK)

    except CustomUser.DoesNotExist:
        context = {
            'message': 'Invalid user_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_leaderboard_entry(request):
    leaderboard_entry_id = request.POST.get('leaderboard_entry_id', None)

    if leaderboard_entry_id is None:
        context = {
            'message': 'leaderboard_entry_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        leaderboard_entry = LeaderboardEntry.objects.get(id=leaderboard_entry_id)
        leaderboard_entry.delete()

        context = {
            'message': f'LeaderboardEntry {leaderboard_entry_id} successfully deleted',
        }
        return Response(context, status=status.HTTP_200_OK)

    except LeaderboardEntry.DoesNotExist:
        context = {
            'message': 'LeaderboardEntry not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        context = {
            'message': 'Invalid leaderboard_entry_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
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
    return Response(entry_data)

@api_view(['GET'])
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
    return Response(entry_list)

