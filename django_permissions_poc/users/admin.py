from django.contrib import admin
from django.contrib.auth.models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "codename",
        "content_type__model",
        "content_type__app_label",
    )
    list_filter = ("content_type__app_label", "content_type__model")
    search_fields = (
        "name",
        "codename",
        "content_type__app_label",
        "content_type__model",
    )
    ordering = ("content_type__app_label", "content_type__model", "codename")
