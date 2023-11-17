from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import CustomUser

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

