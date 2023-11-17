from django.db import models
from countries.models import  Country

class Team(models.Model):
    name=models.CharField(max_length=255)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    captain_name=models.CharField(max_length=255)
    logo=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name