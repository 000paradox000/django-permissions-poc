from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand
from guardian.shortcuts import assign_perm

from django_permissions_poc.operating_systems.models import (
    Distribution,
    OperatingSystem,
)


class Command(BaseCommand):
    help = "Create users."

    def handle(self, *args, **options):
        created = False

        for username, (groups_list, objects_list) in settings.USERS.items():
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

            if objects_list:
                for obj_data in objects_list:
                    cls_name, permissions_list, name = obj_data.split("|")
                    if cls_name == "OperatingSystem":
                        model_cls = OperatingSystem
                    else:
                        model_cls = Distribution

                    obj = model_cls.objects.get(name=name)
                    model_name = model_cls._meta.model_name

                    permissions_list = permissions_list.split(",")
                    for permission in permissions_list:
                        perm = f"operating_systems.{permission}_{model_name}"
                        assign_perm(perm=perm, user_or_group=user, obj=obj)

            created = True

        if created:
            self.stdout.write(self.style.SUCCESS("Users were created."))
        else:
            self.stdout.write("No users were created (they already exist).")
