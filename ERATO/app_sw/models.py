from django.db import models
from django.contrib.auth.models import User

class SW(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    picture_path=models.CharField(max_length=200)
    album_path = models.CharField(max_length=200, default='path')
    MC_path=models.CharField(max_length=200)
    FEMALE = 'female'
    MALE = 'male'
    GENDER_CHOICES = [
        (FEMALE , 'female'),
        (MALE , 'male'),
    ]
    birth_date=models.DateTimeField('date birth')
    weight=models.CharField(max_length=10)
    height=models.CharField(max_length=10)
    about=models.CharField(max_length=500)
    third_email=models.CharField(max_length=50)

class Appearance(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=10, default='name')

class Service(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)