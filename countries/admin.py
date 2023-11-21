from django.contrib import admin
from countries.models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ( 'id','name', 'code', )


admin.site.register(Country,CountryAdmin)
