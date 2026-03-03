from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user

from .models import Distribution, OperatingSystem


class BaseAdmin(GuardedModelAdmin):
    def get_permission(self, name):
        opts = self.model._meta
        return f"{opts.app_label}.{name}_{opts.model_name}"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        perm = self.get_permission("viewall")

        return get_objects_for_user(
            request.user,
            perm,
            klass=qs,
            accept_global_perms=False,
        )

    def has_view_permission(self, request, obj=None):
        if obj is None:
            return True

        perm = self.get_permission("view")
        return request.user.has_perm(perm, obj)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True

        perm = self.get_permission("change")
        return request.user.has_perm(perm, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True

        perm = self.get_permission("delete")
        return request.user.has_perm(perm, obj)

    def has_add_permission(self, request):
        perm = self.get_permission("add")
        return request.user.has_perm(perm)


@admin.register(Distribution)
class DistributionAdmin(BaseAdmin):
    list_display = [
        "id",
        "name",
        "operating_system__name",
    ]


class DistributionInlineAdmin(admin.StackedInline):
    model = Distribution
    extra = 0
    fields = ("name",)


@admin.register(OperatingSystem)
class OperatingSystemAdmin(BaseAdmin):
    list_display = [
        "id",
        "name",
        "get_distributions",
    ]
    inlines = [DistributionInlineAdmin]

    @admin.display(description="distributions")
    def get_distributions(self, obj):
        return ", ".join([d.name for d in obj.distributions.all()])
