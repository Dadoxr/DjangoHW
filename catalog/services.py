from django.conf import settings
from django.core.cache import cache

from catalog.models import Product


def get_all_products_from_cache_or_db():
    
    if settings.CACHE_ENABLE:

        products = cache.get('all_products')
        if products is None:
            products = Product.objects.all()
            cache.set('all_products', products)
    else:
        products = Product.objects.all()
    
    return products