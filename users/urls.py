from django.urls import path
from .views import get_user,get_all_users

urlpatterns = [
    path('users/<int:user_id>/',get_user, name='get_user'),
    path('users/', get_all_users, name='get_all_users'),
]
