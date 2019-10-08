from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    picture_path=models.CharField(max_length=200)#relative to Erato/ERATO
    birth_date=models.DateTimeField('date birth')
# Create your models here.
