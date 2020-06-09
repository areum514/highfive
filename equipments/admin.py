from django.contrib import admin
from . import models
# Register your models here.


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Equiptment)
class EquiptmentAdmin(admin.ModelAdmin):
    """EquiptmentAdmin Admin Definition"""
    inlines = (PhotoInline,)

