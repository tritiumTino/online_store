from django import template
from django.conf import settings
from django.core.cache import cache
from mainapp.models import Category, Product

register = template.Library()


@register.simple_tag()
def get_categories():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = Category.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return Category.objects.filter(is_active=True)


@register.inclusion_tag('online_store/tags/last_products.html')
def get_last_products():
    products = Product.objects.filter(is_active=True)[:4]
    return {'last_products': products}
