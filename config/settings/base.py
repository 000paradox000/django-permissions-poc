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

GROUPS = {
    "Operating System Admin": [
        "operating_systems.add_operatingsystem",
        "operating_systems.change_operatingsystem",
        "operating_systems.delete_operatingsystem",
        "operating_systems.view_operatingsystem",
        "operating_systems.viewall_operatingsystem",
    ],
    "Operating System Owner": [],
    "Operating System Add": [],
    "Operating System Add Owned Only": [],
    "Operating System Change": [],
    "Operating System Change Owned Only": [],
    "Operating System Delete": [],
    "Operating System Delete Owned Only": [],
    "Operating System View": [],
    "Operating System View Owned Only": [],
    "Operating System View All": [],
    "Operating System View All Owned Only": [],
    "Distribution Admin": [
        "operating_systems.add_distribution",
        "operating_systems.change_distribution",
        "operating_systems.delete_distribution",
        "operating_systems.view_distribution",
        "operating_systems.viewall_distribution",
    ],
    "Distribution Owner": [],
    "Distribution Add": [],
    "Distribution Add Owned Only": [],
    "Distribution Change": [],
    "Distribution Change Owned Only": [],
    "Distribution Delete": [],
    "Distribution Delete Owned Only": [],
    "Distribution View": [],
    "Distribution View Owned Only": [],
    "Distribution View All": [],
    "Distribution View All Owned Only": [],
}

USERS = {
    "operatingsystem_admin_1": [
        "Operating System Admin",
    ],
    "operatingsystem_owner_1": [
        "Operating System Owner",
    ],
    "operatingsystem_add_1": [
        "Operating System Add",
    ],
    "operatingsystem_add_owned_only_1": [
        "Operating System Add Owned Only",
    ],
    "operatingsystem_change_1": [
        "Operating System Change",
    ],
    "operatingsystem_change_owned_only_1": [
        "Operating System Change Owned Only",
    ],
    "operatingsystem_delete_1": [
        "Operating System Delete",
    ],
    "operatingsystem_delete_owned_only_1": [
        "Operating System Delete Owned Only",
    ],
    "operatingsystem_view_1": [
        "Operating System View",
    ],
    "operatingsystem_view_owned_only_1": [
        "Operating System View Owned Only",
    ],
    "operatingsystem_viewall_1": [
        "Operating System View All",
    ],
    "operatingsystem_viewall_owned_only_1": [
        "Operating System View All Owned Only",
    ],
    "distribution_admin_1": [
        "Distribution Admin",
    ],
    "distribution_owner_1": [
        "Distribution Owner",
    ],
    "distribution_add_1": [
        "Distribution Add",
    ],
    "distribution_add_owned_only_1": [
        "Distribution Add Owned Only",
    ],
    "distribution_change_1": [
        "Distribution Change",
    ],
    "distribution_change_owned_only_1": [
        "Distribution Change Owned Only",
    ],
    "distribution_delete_1": [
        "Distribution Delete",
    ],
    "distribution_delete_owned_only_1": [
        "Distribution Delete Owned Only",
    ],
    "distribution_view_1": [
        "Distribution View",
    ],
    "distribution_view_owned_only_1": [
        "Distribution View Owned Only",
    ],
    "distribution_viewall_1": [
        "Distribution View All",
    ],
    "distribution_viewall_owned_only_1": [
        "Distribution View All Owned Only",
    ],
}
