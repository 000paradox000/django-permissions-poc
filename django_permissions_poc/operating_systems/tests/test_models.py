import pytest
from django.apps import apps

from conftest import APP_LABEL, MODELS
from django_permissions_poc.common import utilities
from django_permissions_poc.operating_systems.models import (
    Distribution,
    OperatingSystem,
)

pytestmark = pytest.mark.django_db


def test_models_exist_in_app():
    """Verifies that both models are correctly registered in the app."""
    for model in MODELS:
        try:
            apps.get_model(APP_LABEL, model.__name__)
        except LookupError as e:
            pytest.fail(f"Model lookup failed: {e}")


def test_cascade_deletion():
    """Validates that deleting an OS also deletes its Distributions."""
    operating_system = OperatingSystem.objects.create(
        name=utilities.generate_random_string(),
    )
    distros_initial_count = Distribution.objects.count()
    distros_new_count = 2

    for _ in range(distros_new_count):
        Distribution.objects.create(
            name=utilities.generate_random_string(),
            operating_system=operating_system,
        )

    assert Distribution.objects.count() == (
        distros_initial_count + distros_new_count
    )

    # Action: Delete the parent
    operating_system.delete()

    # Assert: Children should be gone
    assert Distribution.objects.count() == distros_initial_count, (
        "Distributions were not deleted on CASCADE"
    )


def test_related_name_works():
    """Checks if the related_name 'distributions' is functional."""
    operating_system = OperatingSystem.objects.create(
        name=utilities.generate_random_string(),
    )
    distro = Distribution.objects.create(
        name=utilities.generate_random_string(),
        operating_system=operating_system,
    )

    assert operating_system.distributions.count() == 1
    assert operating_system.distributions.first().name == distro.name
