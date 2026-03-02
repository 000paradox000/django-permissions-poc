import pytest
from django.urls import reverse

from conftest import ACTIONS, APP_LABEL, MODELS
from django_permissions_poc.common import utilities

pytestmark = pytest.mark.django_db


def test_owner_has_all_model_permissions(django_user_model):
    for model_source in MODELS:
        model_source_name = model_source._meta.model_name
        username = f"{model_source_name}_owner_1"
        user = django_user_model.objects.get(username=username)

        for model_target in MODELS:
            model_target_name = model_target._meta.model_name
            for action in ACTIONS:
                perm_codename = f"{action}_{model_target_name}"
                full_perm = f"{APP_LABEL}.{perm_codename}"

                expected = model_source == model_target
                received = user.has_perm(full_perm)
                msg = f"User: {username}, Perm: {perm_codename}"
                assert received is expected, msg


def test_owner_can_access_owner_pages(django_user_model, client):
    for model_source in MODELS:
        model_source_name = model_source._meta.model_name
        username = f"{model_source_name}_owner_1"
        user = django_user_model.objects.get(username=username)
        assert client.login(username=user.username, password="12345") is True  # noqa: S106

        for model_target in MODELS:
            model_target_name = model_target._meta.model_name
            urlnames = utilities.get_admin_urlnames(APP_LABEL, model_target)

            obj = model_target.objects.first()
            assert obj is not None, f"No objects for '{model_target_name}'"

            status_code = 200 if model_source == model_target else 403

            for name in ACTIONS:
                if name in ["view", "viewall"]:
                    continue

                urlname = urlnames[name]

                if name in ["changelist", "add"]:
                    url = reverse(urlname)
                elif name in ["change", "delete"]:
                    url = reverse(urlname, args=(obj.pk,))
                else:
                    continue

                response = client.get(url)
                assert response.status_code == status_code
