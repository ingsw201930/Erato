from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)
    full_name=models.CharField(max_length=100)
    picture_path = models.CharField(max_length=200)#relative to Erato/ERATO
    mc_path = models.CharField(max_length=200, default="")#relative to Erato/ERATO
    birth_date = models.DateTimeField()
    about=models.CharField(max_length=500, default="")
    email = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=10, decimal_places=3, default=3.000)
