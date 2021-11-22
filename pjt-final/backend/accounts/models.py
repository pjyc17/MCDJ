from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

class Birthday(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='birthday')
    birthday = models.DateField()

# class Profile(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
#     # age = models.PositiveIntegerField()
#     # birth = models.DateTimeField()