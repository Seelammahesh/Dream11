from django.urls import path
from .views import get_country, get_all_countries,add_country,update_country,delete_country

urlpatterns = [
    path('countries/<int:country_id>/', get_country, name='get_country'),
    path('countries/', get_all_countries, name='get_all_countries'),
    path('add_country/', add_country, name="add_country"),
    path('update/<int:id>/', update_country, name="update_country"),
    path('delete/<int:id>/', delete_country, name="delete_country"),

]
