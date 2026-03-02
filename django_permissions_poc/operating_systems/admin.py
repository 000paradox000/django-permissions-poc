from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.contrib import admin, messages
from django.db import transaction
from django.http import HttpResponseRedirect

from .models import Distribution, OperatingSystem


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "operating_system__name",
    ]


class DistributionInlineAdmin(admin.TabularInline):
    model = Distribution
    extra = 0
    fields = ("name",)


@admin.register(OperatingSystem)
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "get_distributions",
    ]
    inlines = [DistributionInlineAdmin]

    @admin.display(description="distributions")
    def get_distributions(self, obj):
        return ", ".join([d.name for d in obj.distributions.all()])
