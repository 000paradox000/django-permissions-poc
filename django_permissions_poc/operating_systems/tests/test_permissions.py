import secrets

import pytest
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

from conftest import ACTIONS, APP_LABEL, MODELS

pytestmark = pytest.mark.django_db


def test_permissions_exist():
    """
    Verifies that Django generated the default permissions for both models.
    """
    for model in MODELS:
        model_name = model.__name__
        meta_model_name = model._meta.model_name
        content_type = ContentType.objects.get_for_model(model)

        for action in ACTIONS:
            codename = f"{action}_{meta_model_name}"

            exists = Permission.objects.filter(
                content_type=content_type,
                codename=codename,
            ).exists()

            msg = (
                f"Permission '{codename}' "
                f"for model '{model_name}' "
                f"does not exist"
            )
            assert exists, msg


def test_user_permission_assignment():
    """Tests if a user can actually hold a permission for these models."""
    staff_user = User.objects.create_user(
        username="staff_user",
        password=secrets.token_urlsafe(16),
    )

    users = [
        staff_user,
        User.objects.get(username="admin"),
    ]

    for user in users:
        # Assign all permissions for all models/actions
        for model in MODELS:
            meta_model_name = model._meta.model_name
            content_type = ContentType.objects.get_for_model(model)

            for action in ACTIONS:
                codename = f"{action}_{meta_model_name}"
                perm = Permission.objects.get(
                    codename=codename,
                    content_type=content_type,
                )
                user.user_permissions.add(perm)

        # Verify user has all permissions
        for model in MODELS:
            model_name = model.__name__
            meta_model_name = model._meta.model_name

            for action in ACTIONS:
                codename = f"{action}_{meta_model_name}"
                permission_name = f"{APP_LABEL}.{codename}"

                msg = (
                    f"Permission '{permission_name}' "
                    f"for model '{model_name}' "
                    f"and user '{user.username}' "
                    f"does not exist"
                )
                assert user.has_perm(permission_name), msg
