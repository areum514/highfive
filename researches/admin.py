from django.contrib import admin
from . import models
# Register your models here.


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Research)
class ResearchAdmin(admin.ModelAdmin):
    """ResearchAdmin Admin Definition"""
    inlines = (PhotoInline,)
