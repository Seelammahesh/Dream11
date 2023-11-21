from django.contrib import admin
from .models import Match,MatchResult

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display=[ 'id','team1','team2','venue']
    search_fields=['venue','date']
    list_filter=['date','venue']

class MatchResultAdmin(admin.ModelAdmin):
    list_display=[ 'match','team1','team2','result']

    
    
admin.site.register(Match,MatchAdmin)
admin.site.register(MatchResult,MatchResultAdmin)