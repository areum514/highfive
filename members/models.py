from django.db import models
from core import models as core_models

# Create your models here.


class Field(core_models.TimeStampedMode):
    """Photo Model Definition"""

    field = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    member = models.ForeignKey(
        "Member", related_name="field", on_delete=models.CASCADE)


class Member(core_models.TimeStampedMode):
    """member Model Definition"""
    name = models.CharField(max_length=140)
    avatar = models.ImageField(upload_to="avatars", blank=True)
