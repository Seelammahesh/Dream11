from django.urls import path
from .views import get_country, get_all_countries

urlpatterns = [
    path('countries/<int:country_id>/', get_country, name='get_country'),
    path('countries/', get_all_countries, name='get_all_countries'),
]
