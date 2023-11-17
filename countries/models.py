from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code=models.CharField(max_length=2 ,unique=True)
    
    
    def __str__(self):
        return self.name
    
