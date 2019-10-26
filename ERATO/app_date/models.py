from django.db import models
from app_client.models import Client
from app_sw.models import Service

class Date(models.Model):
    PAYED = 'payed'
    STARTED = 'started'
    ENDED = 'ended'
    TIMEDOUT='timed out'
    REQUESTED = 'requested'
    ACCEPTED = 'accepted'
    REJECTED= 'rejected'
    RATED='rated'

    STATE_CHOICES = [
        (PAYED , 'payed'),
        (STARTED , 'started'),
        (ENDED , 'ended'),
        (TIMEDOUT , 'timed out'),
        (REQUESTED , 'requested'),
        (ACCEPTED , 'accepted'),
        (REJECTED , 'rejected'),
        (RATED, 'rated')
    ]
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    start_time=models.DateTimeField('start time')
    end_time=models.DateTimeField('end time')
    lat = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    lng = models.DecimalField(max_digits=15, decimal_places=8, default=0.00000000)
    state=models.CharField(max_length=20,choices=STATE_CHOICES,default=REQUESTED)
    price=models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    noise=models.IntegerField(default=None, blank=True, null=True)
