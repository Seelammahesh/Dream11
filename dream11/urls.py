"""
URL configuration for dream11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from countries.views import get_country,get_all_countries
from leaderboard.views import get_leaderboard_entry,get_all_leaderboard_entries
from matches.views import get_match,get_all_matches
from players.views import get_player,get_all_players
from  teams.views import get_team ,get_all_teams
from users.views import get_user,get_all_users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('countries/', include('countries.urls')),
    path('teams/', include('teams.urls')),
    path('players/', include('players.urls')),
    path('matches/', include('matches.urls')),
    path('leaderboard/', include('leaderboard.urls')),

    #countries
    path('countries/<int:country_id>/', get_country, name='get_country'),
    path('countries/', get_all_countries, name='get_all_countries'),

    #leaderboard
    path('leaderboard-entries/<int:entry_id>/', get_leaderboard_entry, name='get_leaderboard_entry'),
    path('leaderboard-entries/', get_all_leaderboard_entries, name='get_all_leaderboard_entries'),
    
    #matches
    path('matches/<int:match_id>/', get_match, name='get_match'),
    path('matches/', get_all_matches, name='get_all_matches'),

    #players
    path('players/<int:player_id>/', get_player, name='get_player'),
    path('players/', get_all_players, name='get_all_players'),

    #teams
    path('teams/<int:team_id>/', get_team, name='get_team'),
    path('teams/', get_all_teams, name='get_all_teams'),

    #users
    path('users/<int:user_id>/',get_user, name='get_user'),
    path('users/', get_all_users, name='get_all_users'),


]
