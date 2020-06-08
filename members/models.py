from django.db import models

# Create your models here.


class member(models.Model):
    """member Model Definition"""
    name = models.CharField(max_length=140)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    description = models.TextField()
