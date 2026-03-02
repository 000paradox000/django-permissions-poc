import pytest
from django.urls import reverse

from conftest import APP_LABEL, MODELS
from django_permissions_poc.common import utilities

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize("model", MODELS)
def test_admin_anonymous_redirects_to_login_for_any_urlname(client, model):
    urlnames = utilities.get_admin_urlnames(APP_LABEL, model)
    admin_login = reverse("admin:login")
    model_name = model._meta.model_name

    obj = model.objects.first()
    assert obj is not None, f"No objects for '{model_name}'"

    for name, urlname in urlnames.items():
        if name in {"change", "delete"}:
            url = reverse(urlname, args=(obj.pk,))
        else:
            url = reverse(urlname)

        resp = client.get(url)

        assert resp.status_code == 302
        assert resp.url.startswith(admin_login)
