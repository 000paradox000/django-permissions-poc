import pytest
from django.core.management import call_command

from django_permissions_poc.operating_systems.models import (
    Distribution,
    OperatingSystem,
)

# ---------------------------------------------------------------------------
# Shared Constants

MODELS = [
    OperatingSystem,
    Distribution,
]

APP_LABEL = "operating_systems"

ACTIONS = ["add", "change", "delete", "view", "viewall"]


# ---------------------------------------------------------------------------
# Initial Commands


@pytest.fixture(scope="session", autouse=True)
def run_initial_management_commands(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("create_admin")
        call_command("create_data")
