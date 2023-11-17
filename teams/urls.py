from django.urls import path
from .views import get_team, get_all_teams

urlpatterns = [
    path('teams/<int:team_id>/', get_team, name='get_team'),
    path('teams/', get_all_teams, name='get_all_teams'),
]
