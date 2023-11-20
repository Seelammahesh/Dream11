from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Match, MatchResult
from teams.models import Team
from countries.models import Country

@api_view(['POST'])
def create_match(request):
    date = request.POST.get('date', None)
    team1_id = request.POST.get('team1_id', None)
    team2_id = request.POST.get('team2_id', None)
    venue = request.POST.get('venue', None)

    if date is None or team1_id is None or team2_id is None or venue is None:
        context = {
            'message': 'date, team1_id, team2_id, or venue is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        team1 = Country.objects.get(id=team1_id)
        team2 = Country.objects.get(id=team2_id)

        match = Match.objects.create(
            date=date,
            team1=team1,
            team2=team2,
            venue=venue,
        )

        data = {
            'message': 'Match created successfully',
            'data': {
                'id': match.id,
                'date': match.date,
                'team1_id': match.team1_id,
                'team2_id': match.team2_id,
                'venue': match.venue,
            }
        }

        return Response(data, status=status.HTTP_201_CREATED)

    except Country.DoesNotExist:
        context = {
            'message': 'Invalid team1_id or team2_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_match(request):
    match_id = request.POST.get('match_id', None)

    if match_id is None:
        context = {
            'message': 'match_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        context = {
            'message': 'Match not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    date = request.POST.get('date', match.date)
    team1_id = request.POST.get('team1_id', match.team1_id)
    team2_id = request.POST.get('team2_id', match.team2_id)
    venue = request.POST.get('venue', match.venue)

    try:
        team1 = Country.objects.get(id=team1_id)
        team2 = Country.objects.get(id=team2_id)

        match.date = date
        match.team1 = team1
        match.team2 = team2
        match.venue = venue
        match.save()

        data = {
            'message': 'Match updated successfully',
            'data': {
                'id': match.id,
                'date': match.date,
                'team1_id': match.team1_id,
                'team2_id': match.team2_id,
                'venue': match.venue,
            }
        }

        return Response(data, status=status.HTTP_200_OK)

    except Country.DoesNotExist:
        context = {
            'message': 'Invalid team1_id or team2_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_match(request):
    match_id = request.POST.get('match_id', None)

    if match_id is None:
        context = {
            'message': 'match_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        match = Match.objects.get(id=match_id)
        match.delete()

        context = {
            'message': f'Match {match_id} successfully deleted',
        }
        return Response(context, status=status.HTTP_200_OK)

    except Match.DoesNotExist:
        context = {
            'message': 'Match not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        context = {
            'message': 'Invalid match_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_match_result(request):
    match_id = request.POST.get('match_id', None)
    team_id = request.POST.get('team_id', None)
    result = request.POST.get('result', None)

    if match_id is None or team_id is None or result is None:
        context = {
            'message': 'match_id, team_id, or result is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        match = Match.objects.get(id=match_id)
        team = Team.objects.get(id=team_id)

        match_result = MatchResult.objects.create(
            match=match,
            team=team,
            result=result,
        )

        data = {
            'message': 'MatchResult created successfully',
            'data': {
                'id': match_result.id,
                'match_id': match_result.match_id,
                'team_id': match_result.team_id,
                'result': match_result.result,
            }
        }

        return Response(data, status=status.HTTP_201_CREATED)

    except Match.DoesNotExist:
        context = {
            'message': 'Invalid match_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except Team.DoesNotExist:
        context = {
            'message': 'Invalid team_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_match_result(request):
    match_result_id = request.POST.get('match_result_id', None)

    if match_result_id is None:
        context = {
            'message': 'match_result_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        match_result = MatchResult.objects.get(id=match_result_id)
    except MatchResult.DoesNotExist:
        context = {
            'message': 'MatchResult not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    match_id = request.POST.get('match_id', match_result.match_id)
    team_id = request.POST.get('team_id', match_result.team_id)
    result = request.POST.get('result', match_result.result)

    try:
        match = Match.objects.get(id=match_id)
        team = Team.objects.get(id=team_id)

        match_result.match = match
        match_result.team = team
        match_result.result = result
        match_result.save()

        data = {
            'message': 'MatchResult updated successfully',
            'data': {
                'id': match_result.id,
                'match_id': match_result.match_id,
                'team_id': match_result.team_id,
                'result': match_result.result,
            }
        }

        return Response(data, status=status.HTTP_200_OK)

    except Match.DoesNotExist:
        context = {
            'message': 'Invalid match_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except Team.DoesNotExist:
        context = {
            'message': 'Invalid team_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_match_result(request):
    match_result_id = request.POST.get('match_result_id', None)

    if match_result_id is None:
        context = {
            'message': 'match_result_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        match_result = MatchResult.objects.get(id=match_result_id)
        match_result.delete()

        context = {
            'message': f'MatchResult {match_result_id} successfully deleted',
        }
        return Response(context, status=status.HTTP_200_OK)

    except MatchResult.DoesNotExist:
        context = {
            'message': 'MatchResult not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        context = {
            'message': 'Invalid match_result_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
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
    return Response(match_data)
@api_view(['GET'])
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
    return Response(match_list, )


def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)


    result_team1 = match.matchresult_set.filter(team=match.team1).first()
    result_team2 = match.matchresult_set.filter(team=match.team2).first()


    if result_team1.result > result_team2.result:
        winner = match.team1
    elif result_team1.result < result_team2.result:
        winner = match.team2
    else:
        winner = None
    context = {
        'match': match,
        'result_team1': result_team1,
        'result_team2': result_team2,
        'winner': winner,
    }

    return Response(context)