from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class SW(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    picture_path=models.CharField(max_length=200)#relative to Erato/ERATO
    MC_path=models.CharField(max_length=200)#relative to Erato/ERATO
    birthDate=models.DateTimeField('date birth')
    status=models.CharField(max_length=20)
    eye_color=models.CharField(max_length=20)



class Service(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    #TODO tags=hay que ver como hacer relacion muchos a muchos en django
    price=models.IntegerField()
# Create your models here.
