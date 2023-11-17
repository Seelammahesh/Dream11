from django.urls import path
from .views import get_leaderboard_entry, get_all_leaderboard_entries

urlpatterns = [
    path('leaderboard-entries/<int:entry_id>/', get_leaderboard_entry, name='get_leaderboard_entry'),
    path('leaderboard-entries/', get_all_leaderboard_entries, name='get_all_leaderboard_entries'),
]
