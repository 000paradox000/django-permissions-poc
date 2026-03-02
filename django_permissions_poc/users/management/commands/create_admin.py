from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create admin."

    def handle(self, *args, **options):
        if User.objects.filter(username="admin").exists():
            return

        User.objects.create_superuser(
            username="admin",
            email="admin@project.local",
            password="12345",
        )

        self.stdout.write(self.style.SUCCESS("Admin user was created."))
