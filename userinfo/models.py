# userinfo/models.py

from django.db import models

class InstagramUser(models.Model):
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    biography = models.TextField()
    profile_pic_url = models.URLField()
