from django.urls import path
from .views import get_match, get_all_matches

urlpatterns = [
    path('matches/<int:match_id>/', get_match, name='get_match'),
    path('matches/', get_all_matches, name='get_all_matches'),
]
