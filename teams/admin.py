from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display=['id','name','logo','country']
    search_fields=['name']
    list_filter=['country']
    
admin.site.register(Team,TeamAdmin)