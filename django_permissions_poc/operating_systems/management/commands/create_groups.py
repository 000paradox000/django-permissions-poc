from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from django_permissions_poc.common import utilities


class Command(BaseCommand):
    help = "Create groups."

    def handle(self, *args, **options):
        has_created = False
        data = settings.GROUPS
        permissions_created = False

        for group_name, permissions_list in data.items():
            obj, created = Group.objects.get_or_create(name=group_name)

            if created:
                has_created = True
                self.stdout.write(f"Group created: {group_name}")

            if permissions_list:
                for permission_name in permissions_list:
                    utilities.add_permission_to_group(
                        group_name,
                        permission_name,
                    )
                    permissions_created = True

        if has_created or permissions_created:
            self.stdout.write(
                self.style.SUCCESS("Create groups process was finished.")
            )
