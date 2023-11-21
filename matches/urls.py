from django.urls import path
from .views import get_all_match_results, get_match_result, get_all_matches,create_match,update_match,delete_match,create_match_result,update_match_result,delete_match_result

urlpatterns = [
    path('get-match-result/<int:match_result_id>/',get_match_result, name='get_match_result'),
    path('get_all_match_results/', get_all_match_results ,name='get_all_match_result'),

    path('matches/', get_all_matches, name='get_all_matches'),
    path('create_match/', create_match, name='create_match'),
    path('update_match/', update_match, name='update_match'),
    path('delete_match/', delete_match, name='delete_match'),
    path('create_match_result/', create_match_result, name='create_match_result'),
    path('update_match_result/', update_match_result, name='update_match_result'),
    path('delete_match_result/', delete_match_result, name='delete_match_result'),
]
