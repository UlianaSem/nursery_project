from django.conf import settings
from django.core.cache import cache

from dogs.models import Breed


def get_breeds_cache():
    if settings.CACHE_ENABLED:
        key = 'breeds_list'
        queryset = cache.get(key)

        if queryset is None:
            queryset = Breed.objects.all()
            cache.set(key, queryset)

    else:
        queryset = Breed.objects.all()

    return queryset
