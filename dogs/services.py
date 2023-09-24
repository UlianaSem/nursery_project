from django.conf import settings
from django.core.cache import cache


class BreedsCacheMixin:

    def get_breeds_cache(self):
        if settings.CACHE_ENABLED:
            key = 'breeds_list'
            queryset = cache.get(key)

            if queryset is None:
                queryset = super().get_queryset()
                cache.set(key, queryset)

        else:
            queryset = super().get_queryset()

        return queryset
