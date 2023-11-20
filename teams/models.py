from django.db import models
from countries.models import  Country
from users.models import CustomUser

AUTH_USER_MODEL='users.CustomUser'

class Team(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,null=True,blank=True)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    captain_name=models.CharField(max_length=255,null=True)
    logo=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name