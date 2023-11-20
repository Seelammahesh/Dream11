from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Country
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework import status
from django.db import  IntegrityError
from  django.core.exceptions import ValidationError

#<------Get-Request- using id------>

@api_view(['GET'])
def get_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    country_data = {
        'id': country.id,
        'name': country.name,
        'code': country.code,
    }
    return JsonResponse(country_data)

#<------Get-Request------->
@api_view(['GET'])
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

#<------POST-Request------->

@api_view(['POST'])
def add_country(request):
    name=request.POST.get('name',None)
    code=request.POST.get('code',None)
    if name is None or code is None:
        context={
            'message':'County name or Country Code is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            country=Country.objects.create(
                name=name,code=code)
            country.save()
            context={
                'message':'New Country added Successfully',
                'data':{
                    'name':country.name,
                    'code':country.code
                }
            }
            return Response(context,status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def update_country(request):
    country_id = request.POST.get('country_id',None)
    name=request.POST.get('name',None)
    code = request.POST.get('code',None)
    if country_id is None or name is None or code is None:
        context={
            'message':'country_id or name or code  is missing'

        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            country = Country.objects.get(id=country_id)
            country.name = name if name is not None else country.name
            country.save()
            context ={
                'message':"Country updated successfully",
                'data':{
                         'name':country.name,
                          'code':country.code
            }
            }
            return Response(context,status=status.HTTP_200_OK)
        except IntegrityError:
            context = {
                'message': 'duplicate entry or invalid_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            context ={
                'message':'invalid category_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_country(request):
    country_id = request.POST.get('country_id',None)
    if country_id is None:
        context ={
            'message':'country_id  is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_country=Country.objects.get(id=country_id)
            get_country.delete()
            context ={
                'message':f'country_id{get_country} sucessfully deleted'
            }
            return Response(context,status=status.HTTP_200_OK)
        except Country.DoesNotExist:
            context={
                'message':'invalid category_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            context ={
                'message':'invalid Country_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
