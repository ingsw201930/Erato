from django.db import models

# Create your models here.
class Service(models.Model):
	id = models.CharField(max_length=50, primary_key=True)
	description =models.CharField(max_length=200)
	price = models.IntegerField()