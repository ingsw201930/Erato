from django.db import models
from django.contrib.auth.models import User

class SW(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    picture_path=models.CharField(max_length=200)
    album_path = models.CharField(max_length=200, default='path')
    MC_path=models.CharField(max_length=200)
    FEMALE = 'Female'
    MALE = 'Male'
    FTM = 'Ftm'
    MTF = 'Mtf'
    OTHER = 'Other'
    GENDER_CHOICES = [
        (FEMALE , 'Female'),
        (MALE , 'Male'),
        (FTM, 'FTM'),
        (MTF, 'MTF'),
        (OTHER, 'Other')
    ]
    birth_date=models.DateTimeField('date birth')
    about=models.CharField(max_length=500)
    third_email=models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=OTHER, null=True)

class Appearance(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    eyes = models.CharField(max_length=10, default='eyes')
    hair = models.CharField(max_length=10, default='hair')
    weight = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    height = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

# Many to many relations, example: https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/
class Tag(models.Model):
    name = models.CharField(max_length=10, default='name')
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)

class Service(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
<<<<<<< HEAD
    description=models.CharField(max_length=400)
    active = models.BooleanField(default=True)
    #TODO tags=hay que ver como hacer relacion muchos a muchos en django
    price=models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    tags=models.ManyToManyField(Tag)
# Create your models here.

=======
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
>>>>>>> master
