from django.urls import path
from .views import get_user,get_all_users,update_user,delete_user,create_user

urlpatterns = [
    path('users/<int:user_id>/',get_user, name='get_user'),
    path('users/', get_all_users, name='get_all_users'),
    path('update_user/', update_user, name='update_user'),
    path('delete_user/', delete_user, name='delete_user'),
    path('create_user/', create_user, name='create_user'),

]
