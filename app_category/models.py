from os import name
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_author')
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name