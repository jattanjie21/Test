from django.db import models
from django.conf import settings


class Social_Links(models.Model):
    # social media links
    facebook_url  = models.URLField(blank=True, null=True, verbose_name="Facebook URL")
    twitter_url   = models.URLField(blank=True, null=True, verbose_name="Twitter URL")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Instagram URL")
    youtube_url   = models.URLField(blank=True, null=True, verbose_name="Youtube URL")
    linkedin_url  = models.URLField(blank=True, null=True, verbose_name="Linkedin URL")
    flickr_url    = models.URLField(blank=True, null=True, verbose_name="Flickr URL")

    class Meta:
        abstract = True


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Validate_User(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        abstract = True

