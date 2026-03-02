import uuid
from collections.abc import Iterable

from django.apps import apps
from django.db.models.base import ModelBase
from django.urls import URLPattern, URLResolver, get_resolver


def get_models_list() -> list[tuple[str, str, str, type[ModelBase]]]:
    """Return all registered Django models with some useful identifiers.

    Each item is:
        (app_label, model_class_name, model_meta_name, model_class)
    """
    models_list: list[tuple[str, str, str, type[ModelBase]]] = []

    for model in apps.get_models():
        app_label = model._meta.app_label
        model_name = model.__name__
        model_meta_name = model._meta.model_name

        models_list.append(
            (
                app_label,
                model_name,
                model_meta_name,
                model,
            )
        )

    return models_list


def generate_random_string() -> str:
    """Generate a random 32-char hex string."""
    return uuid.uuid4().hex


def list_urls() -> list[tuple[str, str]]:
    """List named URL patterns in the project.

    Returns:
        A list of (url_path, view_name) tuples, where view_name is namespaced
        if the URL is inside included resolvers with namespaces.
    """
    resolver = get_resolver()
    urls: list[tuple[str, str]] = []

    def walk_patterns(
        patterns: Iterable[URLPattern | URLResolver],
        *,
        prefix: str = "",
        namespace_prefix: str = "",
    ) -> None:
        for pattern in patterns:
            if isinstance(pattern, URLPattern):
                route = str(pattern.pattern)
                full_url = f"{prefix}{route}"
                view_name = pattern.name or ""

                if view_name and namespace_prefix:
                    namespaced_view_name = f"{namespace_prefix}:{view_name}"
                else:
                    namespaced_view_name = view_name

                # Keep only named URLs
                if namespaced_view_name:
                    urls.append((full_url, namespaced_view_name))
                continue

            # URLResolver
            route = str(pattern.pattern)

            if pattern.namespace:
                new_namespace = (
                    f"{namespace_prefix}:{pattern.namespace}"
                    if namespace_prefix
                    else pattern.namespace
                )
            else:
                new_namespace = namespace_prefix

            walk_patterns(
                pattern.url_patterns,
                prefix=f"{prefix}{route}",
                namespace_prefix=new_namespace,
            )

    walk_patterns(resolver.url_patterns)
    return urls
