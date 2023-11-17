from django.contrib import admin
from leaderboard.models import LeaderboardEntry
# Register your models here.

class LeaderBoardAdmin(admin.ModelAdmin):
    list_display=['user','points']
    search_fields=['user']
    list_filter=['points']


admin.site.register(LeaderboardEntry)