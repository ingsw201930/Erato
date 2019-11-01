from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)
    picture_path = models.CharField(max_length=100)#relative to Erato/ERATO
    birth_date = models.DateTimeField()
    email = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=10, decimal_places=3, default=1.000)
