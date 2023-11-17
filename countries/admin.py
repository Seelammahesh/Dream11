from django.contrib import admin
from countries.models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', )


admin.site.register(Country,CountryAdmin)
