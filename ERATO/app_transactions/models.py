from django.db import models
from app_client.models import Client
from app_sw.models import SW

# Create your models here.
class Transaction(models.Model):
    ACCEPTED = 'accepted'
    REJECTED= 'rejected'
    WAITING= 'waiting'
    STATE_CHOICES = [
    (ACCEPTED , 'accepted'),
    (WAITING , 'waiting'),
    (REJECTED , 'rejected'),
    ]
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=20, default='')
    amount=models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    date = models.DateTimeField('date')
    state=models.CharField(max_length=20,choices=STATE_CHOICES,default=WAITING)
