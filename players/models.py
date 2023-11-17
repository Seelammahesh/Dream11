from django.db import models
from teams.models import Team

class Player(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=50)
    jersey_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name