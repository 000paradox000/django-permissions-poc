from django.core.management.base import BaseCommand

from django_permissions_poc.operating_systems.models import (
    Distribution,
    OperatingSystem,
)


class Command(BaseCommand):
    help = "Create data needed for testing."

    def handle(self, *args, **options):
        has_created = False

        data = {
            "GNU/Linux": ["Debian", "Ubuntu"],
            "Windows": ["Windows 11", "Windows XP"],
            "Mac OS": ["Sequoia", "Sonoma"],
        }

        for os_name, dist_names in data.items():
            os_obj, created = OperatingSystem.objects.get_or_create(
                name=os_name
            )

            if not created:
                continue

            has_created = True

            self.stdout.write(f"OS created: {os_name}")

            for dist_name in dist_names:
                dist_obj, dist_created = Distribution.objects.get_or_create(
                    name=dist_name, operating_system=os_obj
                )

                if not dist_created:
                    continue

                self.stdout.write(f"  - Distro created: {dist_name}")

        if has_created:
            self.stdout.write(self.style.SUCCESS("Process was finished."))
