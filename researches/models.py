from django.db import models

# reverse는 url name을 필요로 하는 funcion으로 url 을 return 함
from django.urls import reverse
from core import models as core_models

# Create your models here.


class Photo(core_models.TimeStampedMode):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    file = models.ImageField(upload_to="research_photos")
    equiptment = models.ForeignKey(
        "Research", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Research(core_models.TimeStampedMode):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Researches"
