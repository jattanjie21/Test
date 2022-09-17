from django.db import models
from utilities.models import TimeStamp
from django.conf import settings
from datetime import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=200, verbose_name='Category Name')
    description   = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class Post(TimeStamp):
    category   = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_title',blank=True,null=True)
    title      = models.CharField(max_length=255,unique=True)
    post_image = models.ImageField(upload_to='blog/',null=True,blank=True)
    content    = models.TextField()
    publish    = models.BooleanField(default=False)
    author     = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='post_author')

    def __str__(self):
        return self.title

    def get_published_date(self):
        if not self.publish:
            return datetime.now()


class AuthorProfile(models.Model):
    pass