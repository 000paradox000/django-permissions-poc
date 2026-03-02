from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create users."

    def handle(self, *args, **options):
        created = False

        for username, groups_list in settings.USERS.items():
            if User.objects.filter(username=username).exists():
                continue

            user = User.objects.create_user(
                username=username,
                password="12345",
                is_staff=True,
            )

            for name in groups_list:
                group = Group.objects.get(name=name)
                user.groups.add(group)

            created = True

        if created:
            self.stdout.write(self.style.SUCCESS("Users were created."))
        else:
            self.stdout.write("No users were created (they already exist).")
