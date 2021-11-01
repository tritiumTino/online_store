from django import template
from mainapp.models import Category, Product

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(is_active=True)


@register.inclusion_tag('online_store/tags/last_products.html')
def get_last_products():
    products = Product.objects.filter(is_active=True)[:4]
    return {'last_products': products}
