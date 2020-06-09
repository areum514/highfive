from django.contrib import admin
from . import models
# Register your models here.


class LinkInline(admin.TabularInline):
    model = models.Link


@admin.register(models.Publication)
class PublicationAdmin(admin.ModelAdmin):
    """PublicationAdmin Admin Definition"""
    inlines = (LinkInline,)
