from django.contrib.admin.apps import AdminConfig


class DjangoPermissionsPOCConfig(AdminConfig):
    default_site = "config.project.admin.DjangoPermissionsPOCAdminSite"
