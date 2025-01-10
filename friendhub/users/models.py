from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=120, unique=True, null=False)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=65)
    profile = models.CharField(default='default.png')