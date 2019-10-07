from django.db import models
from django.contrib.auth.models import User

class SW(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    picture_path=models.CharField(max_length=200)#relative to Erato/ERATO
    MC_path=models.CharField(max_length=200)#relative to Erato/ERATO
    birthDate=models.DateTimeField('date birth')
    weigth=models.CharField(max_length=10)
    heigth=models.CharField(max_length=10)
    about=models.CharField(max_length=500)
    third_email=models.CharField(max_length=200)

class Service(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    #active = models.BooleanField()
    #TODO tags=hay que ver como hacer relacion muchos a muchos en django
    price=models.IntegerField()
# Create your models here.
