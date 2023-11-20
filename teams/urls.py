from django.urls import path
from .views import get_team, get_all_teams,create_team,update_team,delete_team

urlpatterns = [
    path('teams/<int:team_id>/', get_team, name='get_team'),
    path('teams/', get_all_teams, name='get_all_teams'),
    path('create_team/', create_team, name='create_team'),
    path('update_team/', update_team, name='update_team'),
    path('delete_team/', delete_team, name='delete_team'),
]
