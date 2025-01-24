from django.db import models
from users.models import Profile
# Create your models here.
from datetime import datetime
from users.models import Profile


class Chirp(models.Model):
    # like a tweet or a blog post
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    engagement = models.IntegerField('Engage Count', default=1)
    # date_updated = models.DateTimeField
    # viewed = this will tell who already seen the post

    def __str__(self):
        return self.content[:20] + '...'
    
    def add_chirp(self):
        self.save()


class Comments(models.Model):
    post = models.ForeignKey(Chirp, on_delete=models.CASCADE)
    # user = models.ForeignKey(Profile, )
    content = models.CharField(max_length=128)
    date_posted  = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.content[:20] + '...'
    
    def add(self):
        self.save()
        