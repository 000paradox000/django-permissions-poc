# -----------------------------------------------------------------------------
# Environment variables

DJANGO_BASE_DIR := $(CURDIR)
DJANGO_PROJECT_DIR := $(DJANGO_BASE_DIR)/django_permissions_poc
DJANGO_DB_DIR := $(DJANGO_PROJECT_DIR)/db

# -----------------------------------------------------------------------------
# Versions

python.version.local:
	@python -c "import sys; print(sys.version)"

django.version.local:
	@python -c "import django; print(django.get_version())"

# -----------------------------------------------------------------------------
# Requirements

requirements.install.%:
	pip install --upgrade pip
	pip install -r requirements/$*.txt

# -----------------------------------------------------------------------------
# Linter

linter.install.%:
	pre-commit install

linter.update.%:
	pre-commit autoupdate

linter.run.%:
	pre-commit run --all-files
	pre-commit run --all-files

# -----------------------------------------------------------------------------
# Django

django.run.%:
	python manage.py runserver 0.0.0.0:9600 \
		--settings=config.settings.$*

django.shell.%:
	python manage.py shell \
		--settings=config.settings.$*

django.migrations.%:
	python manage.py makemigrations \
		--settings=config.settings.$*
	python manage.py migrate \
		--settings=config.settings.$*

django.create_admin.%:
	python manage.py create_admin \
		--settings=config.settings.$*

django.create_groups.%:
	python manage.py create_groups \
		--settings=config.settings.$*

django.create_data.%:
	python manage.py create_data \
		--settings=config.settings.$*

django.create_users.%:
	python manage.py create_users \
		--settings=config.settings.$*

django.collectstatic.%:
	python manage.py collectstatic \
		--noinput \
		--settings=config.settings.$*

django.init.%:
	make requirements.install.$*
	make django.migrations.$*
	make django.create_admin.$*
	make django.create_groups.$*
	make django.create_data.$*
	make django.create_users.$*
	make django.collectstatic.$*

django.reset.%:
	rm -rf $(DJANGO_DB_DIR)/*.db
	find $(DJANGO_PROJECT_DIR) -path "*/migrations/*.py" ! -name "__init__.py" -delete
	make django.init.$*

# -----------------------------------------------------------------------------
# Tests

tests.run.%:
	pytest \
		--ds=config.settings.$*

tests.functional.run.%:
	pytest \
		-m "functional" \
		--ds=config.settings.$*

tests.not_functional.run.%:
	pytest \
		-m "not functional" \
		--ds=config.settings.$*

# -----------------------------------------------------------------------------
# Coverage using Django test runner

coverage.run.%:
	coverage erase
	coverage run \
		-m pytest \
		--ds=config.settings.$*
	coverage report \
		-m

coverage.not_functional.run.%:
	coverage erase
	coverage run \
		-m pytest \
		-m "not functional" \
		--ds=config.settings.$*
	coverage report \
		-m

coverage.functional.run.%:
	coverage erase
	coverage run \
		-m pytest \
		-m "functional" \
		--ds=config.settings.$*
	coverage report \
		-m
