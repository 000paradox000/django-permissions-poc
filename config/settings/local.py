from .base import *

# ------------------------------------------------------------------------------

DEBUG = True
ENVIRONMENT_SLUG_NAME = "Local"

ALLOWED_HOSTS: list[str] = ["*"]

WSGI_APPLICATION = "config.wsgi.local.application"

# ------------------------------------------------------------------------------

DATABASES: dict = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": PROJECT_DIR / "db" / "django_permissions_poc.db",
    }
}

# ------------------------------------------------------------------------------

SITE_TITLE = f"[{ENVIRONMENT_SLUG_NAME}] {SITE_TITLE}"
SITE_HEADER = f"[{ENVIRONMENT_SLUG_NAME}] {SITE_HEADER}"

# ------------------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = TEMPORAL_DIR / "email"

# ------------------------------------------------------------------------------

FULL_URL = "http://localhost:9600"
