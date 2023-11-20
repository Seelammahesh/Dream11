from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import CustomUser


@api_view(['POST'])
def create_user(request):
    username = request.data.get('username', None)
    email = request.data.get('email', None)
    profile_picture = request.FILES.get('profile_picture', None)
    bio = request.data.get('bio', None)
    date_of_birth = request.data.get('date_of_birth', None)

    if username is None or email is None:
        context = {
            'message': 'username or email is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.create(
            username=username,
            email=email,
            profile_picture=profile_picture,
            bio=bio,
            date_of_birth=date_of_birth,
        )

        data = {
            'message': 'User created successfully',
            'data': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'profile_picture': user.profile_picture.url if user.profile_picture else None,
                'bio': user.bio,
                'date_of_birth': user.date_of_birth,
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
def update_user(request):
    user_id = request.POST.get('user_id', None)
    email = request.POST.get('email', None)
    profile_picture = request.FILES.get('profile_picture', None)
    bio = request.POST.get('bio', None)
    date_of_birth = request.POST.get('date_of_birth', None)

    if user_id is None or email is None:
        context = {
            'message': 'user_id or email is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(id=user_id)
        user.email = email
        user.profile_picture = profile_picture if profile_picture is not None else user.profile_picture
        user.bio = bio if bio is not None else user.bio
        user.date_of_birth = date_of_birth if date_of_birth is not None else user.date_of_birth
        user.save()

        data = {
            'message': 'User updated successfully',
            'data': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'profile_picture': user.profile_picture.url if user.profile_picture else None,
                'bio': user.bio,
                'date_of_birth': user.date_of_birth,
            }
        }

        return Response(data, status=status.HTTP_200_OK)

    except IntegrityError:
        context = {
            'message': 'Duplicate entry or invalid data',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    except ValueError:
        context = {
            'message': 'Invalid user_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request):
    user_id = request.POST.get('user_id', None)

    if user_id is None:
        context = {
            'message': 'user_id is missing',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()

        context = {
            'message': f'User {user_id} successfully deleted',
        }
        return Response(context, status=status.HTTP_200_OK)

    except CustomUser.DoesNotExist:
        context = {
            'message': 'User not found',
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)

    except ValueError:
        context = {
            'message': 'Invalid user_id',
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'profile_picture': user.profile_picture.url if user.profile_picture else None,
        'bio': user.bio,
        'date_of_birth': user.date_of_birth,
    }
    return JsonResponse(user_data)
@api_view(['GET'])
def get_all_users(request):
    users = CustomUser.objects.all()
    user_list = [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'profile_picture': user.profile_picture.url if user.profile_picture else None,
            'bio': user.bio,
            'date_of_birth': user.date_of_birth,
        }
        for user in users
    ]
    return JsonResponse(user_list, safe=False)

