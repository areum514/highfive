from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.ParticipatingSociety, models.ReserchArea, models.CooperativeResearchInstitution)
class ItemAdim(admin.ModelAdmin):
    """Item Admin Definition"""
    list_display = ("name",)


@admin.register(models.Description)
class DescriptionAdmin(admin.ModelAdmin):
    """DescriptionAdmin Admin Definition"""
    filter_horizontal = (
        "participating_societies",
        "reserch_areas",
        "cooperative_research_institutions",
    )
