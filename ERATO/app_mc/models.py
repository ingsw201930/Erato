from django.db import models

# Create your models here.
class MC(models.Model):
    VERIFYING = 'verifying'
    VALID = 'valid'

    STATE_CHOICES = [
        (VERIFYING , 'verifying'),
        (VALID , 'valid'),
    ]

    file_path = models.CharField(max_length=100, default='path')
    last_date=models.DateTimeField('start time')
    state = models.CharField(max_length=100, default=VERIFYING)

    def __str__(self):
        return self.file_path
