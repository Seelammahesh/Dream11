from django.db import models
from teams.models import Team
from countries.models import Country



class Match(models.Model):
    date = models.DateTimeField()
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    venue = models.CharField(max_length=255,null=True,choices=[
        ('Chinnaswamy','Chinnaswamy'),('Mohali','Mohali'),('Narendra-modi','Narendra-modi'),
        ('mumbai-Wankhede','mumbai-Wankhade'),('Chennai-chepauk','Chennai-Chepauk'),('Kolkata-Eden-gardens','Kolkata-Eden-gardens')
    ])

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date}"


class MatchResult(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name='match_result_team1', on_delete=models.CASCADE,null=True)
    team2 = models.ForeignKey(Team, related_name='match_result_team2', on_delete=models.CASCADE,null=True)
    result = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.result}"


