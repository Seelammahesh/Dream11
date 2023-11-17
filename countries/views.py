from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Country

def get_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    country_data = {
        'id': country.id,
        'name': country.name,
        'code': country.code,
    }
    return JsonResponse(country_data)

def get_all_countries(request):
    countries = Country.objects.all()
    country_list = [
        {
            'id': country.id,
            'name': country.name,
            'code': country.code,
        }
        for country in countries
    ]
    return JsonResponse(country_list, safe=False)

