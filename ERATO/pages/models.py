from django.db import models

class SW(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture_path=models.CharField(max_length=200)#relative to Erato/ERATO
    MC_path=models.CharField(max_length=200)#relative to Erato/ERATO
    birthDate=models.DateTimeField('date published')
    statue=models.CharField(max_length=20)
    eye_color=models.CharField(max_length=20)
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        SW.objects.create(user=instance)

@reciever(post_save,sender=User)
def save_user_profile(sender,instance,created,**kwargs):
    instance.profile.save()

class Service(models.Model):
    sw = models.ForeignKey(SW, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    #TODO tags=hay que ver como hacer relacion muchos a muchos en django
    price=models.IntegerField()
# Create your models here.
