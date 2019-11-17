from django.db import models
from django.contrib.auth.models import User
from app_mc.models import MC

class SW(models.Model):
    FEMALE = 'Femenino'
    MALE = 'Masculino'
    FTM = 'Ftm'
    MTF = 'Mtf'
    OTHER = 'Otro'

    GENDER_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (FTM, 'FTM'),
        (MTF, 'MTF'),
        (OTHER, 'Other')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100)
    about = models.CharField(max_length=500)
    mc = models.OneToOneField(MC,on_delete = models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=OTHER, null=True)
    birth_date = models.DateTimeField('date birth')
    third_email = models.CharField(max_length=50)
    picture_path = models.CharField(max_length=200)
    album_path = models.CharField(max_length=200, default='path')

class AdditionalImage(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    extra_picture_path = models.CharField(max_length=500)

class Appearance(models.Model):

    # Eyes
    BLUE = 'Azul'
    BROWN = 'Café'
    GREEN = 'Verde'
    HAZEL = 'Hazel'
    GRAY = 'Gris'
    AMBER = 'Amber'

    # Hair color
    DARK = 'Oscuro'
    CARAMEL = 'Caramel'
    BLONDE = 'Rubio'
    WHITE = 'White'
    COLORFUL = 'Colorido'

    # Hair style
    BOB = 'Bob'
    LONG = 'Largo'

    # Skin color
    S_1 = "#FFDBAC"
    S_2 = "#F1C27D"


    OTHER = 'Other'

    EYES_CHOICES = [
        (BLUE, 'Azul'),
        (BROWN, 'Café'),
        (GREEN, 'Verde'),
        (HAZEL, 'Hazel'),
        (GRAY, 'Gris'),
        (AMBER, 'Amber'),
        (OTHER, 'Otro')
    ]

    HAIR_COLOR_CHOICES = [
        (DARK, 'Oscuro'),
        (BLONDE, 'Rubio'),
        (OTHER, 'Otro')
    ]

    HAIR_STYLES_CHOICES = [
        (BOB, 'Bob'),
        (LONG, 'Largo'),
        (OTHER, 'Otro')
    ]

    SKIN_CHOICES = [
        (S_1, '#FFDBAC'),
        (S_2, '#F1C27D'),
        # (3, '#E0AC69'),
        # (4, '#C68642'),
        # (5, '#8D5524'),
        # (6, '#260701'),
    ]

    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    eyes = models.CharField(max_length=10, choices=EYES_CHOICES, default=OTHER)
    hair_color = models.CharField(max_length=10, choices=HAIR_COLOR_CHOICES, default=OTHER)
    hair_style = models.CharField(max_length=10, choices=HAIR_STYLES_CHOICES, default=OTHER)
    skin = models.CharField(max_length=10, choices=SKIN_CHOICES, default=OTHER)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

# Many to many relations, example: https://docs.djangoproject.com/en/2.2/topics/db/examples/many_to_many/
class Tag(models.Model):
    name = models.CharField(max_length=19, default='name')
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Service(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
