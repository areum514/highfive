from django.db import models

# reverse는 url name을 필요로 하는 funcion으로 url 을 return 함
from django.urls import reverse
from core import models as core_models

# Create your models here.


class Photo(core_models.TimeStampedMode):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="equiptment_photos")
    equiptment = models.ForeignKey(
        "Equiptment", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Equiptment(core_models.TimeStampedMode):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def first_photo(self):
        try:
            photo = self.photos
        except ValueError:
            return None
        return photo.file.url
