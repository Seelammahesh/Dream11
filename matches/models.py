from django.db import models
from teams.models import Team

class Match(models.Model):
    date = models.DateTimeField()
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    venue = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date}"
