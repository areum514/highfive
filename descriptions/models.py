from django.db import models
from core import models as core_models

# Create your models here.


class AbstractItem(core_models.TimeStampedMode):
    """Abract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ParticipatingSociety(AbstractItem):
    """ParticipatingSociety Model Definition"""

    class Meta:
        verbose_name_plural = "Participating Societies"


class CooperativeResearchInstitution(AbstractItem):
    """CooperativeResearchInstitution Model Definition"""
    pass


class ReserchArea(AbstractItem):
    photo = models.ImageField(upload_to="photos", blank=True)
    description = models.TextField(default="")

    class Meta:
        verbose_name_plural = "Reserch Areas"


class Description(core_models.TimeStampedMode):
    """Description Model Definition"""

    adress = models.CharField(max_length=80, default="")
    email = models.CharField(max_length=20, default="")
    contact_number = models.CharField(max_length=20, default="")
    description = models.TextField(default="")

    participating_societies = models.ManyToManyField(
        ParticipatingSociety, related_name="Description", blank=True)
    reserch_areas = models.ManyToManyField(
        ReserchArea, related_name="Description", blank=True)
    cooperative_research_institutions = models.ManyToManyField(
        CooperativeResearchInstitution, related_name="Description", blank=True)
