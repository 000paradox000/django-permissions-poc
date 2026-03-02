import pytest
from django.conf import settings
from django.contrib.auth.models import User

from django_permissions_poc.operating_systems.models import (
    Distribution,
    OperatingSystem,
)

pytestmark = pytest.mark.django_db


def test_database_data_created():
    """Verifies OS and Distributions were created correctly."""
    for os_name, distros in settings.DATA.items():
        os_obj = OperatingSystem.objects.get(name=os_name)

        db_distros = Distribution.objects.filter(
            operating_system=os_obj
        ).values_list("name", flat=True)

        assert set(db_distros) == set(distros)


def test_admin_user():
    u = User.objects.get(username="admin")

    assert u.is_staff is True
    assert u.is_active is True
    assert u.is_superuser is True
