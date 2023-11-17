from django.contrib import admin
from matches.models import Match

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display=['team1','team2','venue']
    search_fields=['venue','date']
    list_filter=['date','venue']
    
    
admin.site.register(Match,MatchAdmin)