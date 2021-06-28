from django.db import models
from django.contrib.auth.models import User

# function to rename the image
def image_location(instance, filename):
    ex = filename.split('.')[-1]
    return 'users/%s.%s' % (instance.user.username, ex)

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    image = models.ImageField(upload_to=image_location)
    bio = models.TextField(blank=True)
    twitter = models.CharField(default='#', max_length=200)
    facebook = models.CharField(default='#', max_length=200)
    instagram = models.CharField(default='#', max_length=200)
    linkedin = models.CharField(default='#', max_length=200)
    github = models.CharField(default='#', max_length=200)

    def __str__(self):
        return self.user.username