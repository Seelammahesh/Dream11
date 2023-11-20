from django.db import models
from users.models import CustomUser


class LeaderboardEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    points = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ['-points']  # Default order for queries
        indexes = [
            models.Index(fields=['points']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.points} points"