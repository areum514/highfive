from django.contrib import admin
from . import models
# Register your models here.


class FieldInline(admin.TabularInline):
    model = models.Field


@admin.register(models.Member)
class MemberAdim(admin.ModelAdmin):
    """Item Admin Definition"""
    list_display = ("name", )

    def __str__(self):
        return self.name
