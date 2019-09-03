from django.db import models

class SW(models.Model):
    email = models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    picture_path=models.CharField(max_length=200)#relative to Erato/ERATO
    MC_path=models.CharField(max_length=200)#relative to Erato/ERATO
    birthDate=models.DateTimeField('date published')
    statue=models.CharField(max_length=20)
    eye_color=models.CharField(max_length=20)


class Service(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    #TODO tags=hay que ver como hacer relacion muchos a muchos en django
    price=models.IntegerField()
# Create your models here.
