import pytest
from django.urls import reverse

from conftest import ACTIONS, APP_LABEL, MODELS

pytestmark = pytest.mark.django_db


@pytest.fixture()
def superadmin(django_user_model):
    return django_user_model.objects.get(username="admin")


@pytest.mark.parametrize("model", MODELS)
@pytest.mark.parametrize("action", ACTIONS)
def test_superadmin_has_all_model_permissions(superadmin, model, action):
    model_name = model._meta.model_name
    perm_codename = f"{action}_{model_name}"
    full_perm = f"{APP_LABEL}.{perm_codename}"

    assert superadmin.has_perm(full_perm) is True


@pytest.mark.parametrize("model", MODELS)
def test_superadmin_can_access_admin_pages(client, superadmin, model):
    assert client.login(username=superadmin.username, password="12345") is True  # noqa: S106

    model_name = model._meta.model_name
    obj = model.objects.first()
    assert obj is not None, f"No objects for '{model_name}'"

    urlnames = {
        "changelist": f"admin:{APP_LABEL}_{model_name}_changelist",
        "add": f"admin:{APP_LABEL}_{model_name}_add",
        "change": f"admin:{APP_LABEL}_{model_name}_change",
        "delete": f"admin:{APP_LABEL}_{model_name}_delete",
    }

    # changelist / add
    assert client.get(reverse(urlnames["changelist"])).status_code == 200
    assert client.get(reverse(urlnames["add"])).status_code == 200

    # change / delete need pk
    assert (
        client.get(reverse(urlnames["change"], args=(obj.pk,))).status_code
        == 200
    )
    assert (
        client.get(reverse(urlnames["delete"], args=(obj.pk,))).status_code
        == 200
    )
