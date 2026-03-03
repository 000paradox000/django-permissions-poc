from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user

from .models import Distribution, OperatingSystem


class BaseAdmin(GuardedModelAdmin):
    # Action name used for list filtering
    list_permission_codename = "viewall"

    def get_permission_string(self, action):
        opts = self.model._meta
        return f"{opts.app_label}.{action}_{opts.model_name}"

    def has_permission_logic(self, request, action, obj=None):
        perm = self.get_permission_string(action)

        # Check for global permission (True for superusers or staff with
        # global rights)
        if request.user.has_perm(perm):
            return True

        # If no object is provided (e.g., when loading the list view),
        # we return True to allow the user into the room.
        # The 'get_queryset' will then handle filtering out what they
        # shouldn't see.
        if obj is None:
            return True

        # Check for the specific object permission via Guardian
        return request.user.has_perm(perm, obj)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        # Use 'viewall' (or whatever you set) to filter the rows
        perm = self.get_permission_string(self.list_permission_codename)

        qs = get_objects_for_user(
            user=request.user,
            perms=perm,
            klass=qs,
            accept_global_perms=False,
        )

        return qs

    def has_view_permission(self, request, obj=None):
        # We check 'view' (standard) or your custom 'viewall'
        return self.has_permission_logic(request, "view", obj)

    def has_change_permission(self, request, obj=None):
        return self.has_permission_logic(request, "change", obj)

    def has_delete_permission(self, request, obj=None):
        return self.has_permission_logic(request, "delete", obj)

    def has_add_permission(self, request):
        # 'Add' never has an 'obj', so it checks the global permission
        perm = self.get_permission_string("add")
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
