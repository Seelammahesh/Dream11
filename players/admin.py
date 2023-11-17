from django.contrib import admin
from .models import Player

# Register your models here.
class playerAdmin(admin.ModelAdmin):
    list_display=('id','name','team','jersey_number','team')

admin.site.register(Player,playerAdmin)