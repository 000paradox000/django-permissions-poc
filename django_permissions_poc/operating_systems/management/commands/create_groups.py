from django.conf import settings
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create groups."

    def handle(self, *args, **options):
        has_created = False
        data = settings.GROUPS

        for group_name, _ in data.items():
            obj, created = Group.objects.get_or_create(name=group_name)

            if not created:
                continue

            has_created = True

            self.stdout.write(f"Group created: {group_name}")

        if has_created:
            self.stdout.write(self.style.SUCCESS("Process was finished."))
