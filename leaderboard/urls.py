from django.urls import path
from .views import get_leaderboard_entry,create_leaderboard_entry,delete_leaderboard_entry,get_all_leaderboard_entries,update_leaderboard_entry

urlpatterns = [
    path('leaderboard-entries/<int:entry_id>/', get_leaderboard_entry, name='get_leaderboard_entry'),
    path('leaderboard-entries/', get_all_leaderboard_entries, name='get_all_leaderboard_entries'),
    path('create_leaderboard_entry/', create_leaderboard_entry, name='create_leaderboard_entry'),
    path('update_leaderboard_entry/', update_leaderboard_entry, name='update_leaderboard_entry'),
    path('delete_leaderboard_entry/', delete_leaderboard_entry, name='delete_leaderboard_entry'),
]
