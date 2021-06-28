from app_category.models import Category
from django.contrib.auth.models import User
from django.db import models

# function to rename the image
def image_location(instance, filename):
    ex = filename.split('.')[-1]
    return 'posts/%s.%s' % (instance.slug, ex)

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='post_author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, related_name='post_category')
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=50, unique=True)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=image_location)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)