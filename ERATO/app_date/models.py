from django.db import models
from app_client.models import Client
from app_sw.models import Service

# Create your models here.
class Date(models.Model):
    client=models.OneToOneField(Client,on_delete=models.CASCADE)
    service=models.OneToOneField(Service,on_delete=models.CASCADE)
    start=models.DateTimeField('start time')
    end=models.DateTimeField('end time')
    place=models.CharField(max_length=200)#this mous change
    state=models.CharField(max_length=20)#pre-pay,payed,started,ended,timed out
