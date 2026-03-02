import environ

from .original import *

# -----------------------------------------------------------------------------
# Paths

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR / "django_permissions_poc"

# -----------------------------------------------------------------------------
# Environment variables

env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR / ".env")

SECRET_KEY = env("DJANGO_SECRET_KEY", default="12345")

# -----------------------------------------------------------------------------
# Default Data Types

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------------------------------------------
# Application definition

DJANGO_APPS = INSTALLED_APPS
DJANGO_APPS[0] = "config.project.apps.DjangoPermissionsPOCConfig"

THIRD_PARTY_APPS = [
    "admin_extra_buttons",
    "rest_framework",
    "drf_spectacular",
]
LOCAL_APPS = [
    "django_permissions_poc.common.apps.CommonConfig",
    "django_permissions_poc.users.apps.UsersConfig",
    "django_permissions_poc.operating_systems.apps.OperatingSystemsConfig",
    "django_permissions_poc.api.apps.APIConfig",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# -----------------------------------------------------------------------------
# Templates

TEMPLATES[0]["DIRS"] = [
    PROJECT_DIR / "templates",
]

# -----------------------------------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_TZ = True

# -----------------------------------------------------------------------------
# Static

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    PROJECT_DIR / "static",
]
STATIC_ROOT = PROJECT_DIR / "static_root"

# -----------------------------------------------------------------------------
# Media

MEDIA_URL = "/media/"
MEDIA_ROOT = PROJECT_DIR / "media"

# -----------------------------------------------------------------------------
# Paths

TEMPORAL_DIR = PROJECT_DIR / "temporal"
FILES_DIR = PROJECT_DIR / "files"
INPUT_FILES_DIR = FILES_DIR / "input"
OUTPUT_FILES_DIR = PROJECT_DIR / "output"
TEST_FIXTURES_DIR = INPUT_FILES_DIR / "test_fixtures"
INTERESTS_DIR = INPUT_FILES_DIR / "interests"

# -----------------------------------------------------------------------------
# Site title

SITE_TITLE = "Django Permissions POC"
SITE_HEADER = "Django Permissions POC"

# -----------------------------------------------------------------------------
# Admins

ADMINS = []

# -----------------------------------------------------------------------------
# Data

DATA = {
    "GNU/Linux": ["Debian", "Ubuntu"],
    "Windows": ["Windows 11", "Windows XP"],
    "Mac OS": ["Sequoia", "Sonoma"],
}
