from django.urls import path
from .views import get_match, get_all_matches,match_detail,create_match,update_match,delete_match,create_match_result,update_match_result,delete_match_result

urlpatterns = [
    path('matches/<int:match_id>/', get_match, name='get_match'),
    path('matches/', get_all_matches, name='get_all_matches'),
    path('match-detail/',match_detail,name="match_detail"),
    path('create_match/', create_match, name='create_match'),
    path('update_match/', update_match, name='update_match'),
    path('delete_match/', delete_match, name='delete_match'),
    path('create_match_result/', create_match_result, name='create_match_result'),
    path('update_match_result/', update_match_result, name='update_match_result'),
    path('delete_match_result/', delete_match_result, name='delete_match_result'),
]
