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

from countries.views import get_country,get_all_countries,add_country,delete_country,update_country

from leaderboard.views import get_leaderboard_entry,get_all_leaderboard_entries,create_leaderboard_entry,delete_leaderboard_entry,get_all_leaderboard_entries,update_leaderboard_entry

from matches.views import get_match,get_all_matches,match_detail,create_match,update_match,delete_match,create_match_result,update_match_result,delete_match_result

from players.views import get_player,get_all_players,update_player,delete_player,create_player

from  teams.views import get_team ,get_all_teams,create_team,update_team,delete_team

from users.views import get_user,get_all_users,update_user,delete_user,create_user


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
    path('add_country/', add_country, name="add_country"),
    path('update/<int:id>/', update_country, name="update_country"),
    path('delete/<int:id>/', delete_country, name="delete_country"),

    #leaderboard
    path('leaderboard-entries/<int:entry_id>/', get_leaderboard_entry, name='get_leaderboard_entry'),
    path('leaderboard-entries/', get_all_leaderboard_entries, name='get_all_leaderboard_entries'),
    path('create_leaderboard_entry/', create_leaderboard_entry, name='create_leaderboard_entry'),
    path('update_leaderboard_entry/', update_leaderboard_entry, name='update_leaderboard_entry'),
    path('delete_leaderboard_entry/', delete_leaderboard_entry, name='delete_leaderboard_entry'),
    
    #matches
    path('matches/<int:match_id>/', get_match, name='get_match'),
    path('matches/', get_all_matches, name='get_all_matches'),
    path('match-detail/',match_detail,name="match_detail"),
    path('create_match/', create_match, name='create_match'),
    path('update_match/', update_match, name='update_match'),
    path('delete_match/', delete_match, name='delete_match'),
    path('create_match_result/', create_match_result, name='create_match_result'),
    path('update_match_result/', update_match_result, name='update_match_result'),
    path('delete_match_result/', delete_match_result, name='delete_match_result'),

    #players
    path('players/<int:player_id>/', get_player, name='get_player'),
    path('players/', get_all_players, name='get_all_players'),
    path('update_player/<int:player_id>/', update_player, name='update_player'),
    path('delete_player/<int:player_id>/', delete_player, name='delete_player'),
    path('create_player/', create_player, name='create_player'),


    #teams
    path('teams/<int:team_id>/', get_team, name='get_team'),
    path('teams/', get_all_teams, name='get_all_teams'),
    path('create_team/', create_team, name='create_team'),
    path('update_team/', update_team, name='update_team'),
    path('delete_team/', delete_team, name='delete_team'),

    #users
    path('users/<int:user_id>/',get_user, name='get_user'),
    path('users/', get_all_users, name='get_all_users'),
    path('update_user/', update_user, name='update_user'),
    path('delete_user/', delete_user, name='delete_user'),
    path('create_user/', create_user, name='create_user'),


]
