from django.db import models

# reverse는 url name을 필요로 하는 funcion으로 url 을 return 함
from django.urls import reverse
from core import models as core_models

# Create your models here.


class Link(core_models.TimeStampedMode):
    """Photo Model Definition"""

   # caption = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    url = models.URLField(("link"), max_length=200, blank=True, null=True)
    publication = models.ForeignKey(
        "Publication", related_name="link", on_delete=models.CASCADE)


class Publication(core_models.TimeStampedMode):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
