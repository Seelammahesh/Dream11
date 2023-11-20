from django.db import models
from teams.models import Team
from matches.models import Match
from countries.models import Country

class Player(models.Model):
    name = models.CharField(max_length=255,null=True)
    country=models.ForeignKey(Country,null=True,on_delete=models.CASCADE)
    age=models.IntegerField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    jersey_number = models.PositiveIntegerField(unique=True,null=True)
    batting_style = models.CharField(max_length=255,null=True,blank=True, choices=[('Right-hand batsmen', 'Right-hand batsmen')
        , ('Left-hand batsmen', 'Left-hand batsmen')])

    bowling_style = models.CharField(max_length=255,null=True,blank=True,choices=[('Right-arm fast', 'Right-arm fast')
        , ('Left-arm fast', 'Left-arm fast'),('Left-arm medium','Left-arm medium'),('Right-arm medium','Right-arm medium'),
                                                              ('Left-arm spin','Left-arm spin'),('Right-arm spin','Right-arm spin')])
    player_type=models.CharField(max_length=255,null=True,blank=True,choices=[('Batsmen','Batsmen'),('Bowler','Bowler'),('All-rounder','All-rounder'),('Batsmen-Wicketkeeper','Batsmen-Wicketkeeper')])

    is_captain=models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.name

class PlayerMatchPoints(models.Model):
    player=models.ForeignKey(Country,on_delete=models.CASCADE)
    match=models.ForeignKey(Match,on_delete=models.CASCADE)
    points=models.IntegerField(null=True,blank=True)