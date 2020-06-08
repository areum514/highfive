from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.member)
class MemberAdim(admin.ModelAdmin):
    """Item Admin Definition"""
    list_display = ("name", )

    def __str__(self):
        return self.name
