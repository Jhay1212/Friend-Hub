from django.db import models

# models.Abs

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=120, unique=True, null=False)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=65)
    profile = models.CharField(default='default.png', max_length=128)

    def __str__(self):
        return self.username.title()
class Followers(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    


class Follows(models.Model):
    pass