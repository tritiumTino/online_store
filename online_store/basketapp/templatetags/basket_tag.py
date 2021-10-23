from django import template
from basketapp.models import Basket

register = template.Library()


@register.simple_tag()
def get_basket(user):
    if user.is_authenticated:
        basket = Basket.objects.filter(user=user)
        total = list(basket)[0].get_total_quantity
        return {'basket': basket, 'total': total}
    return None
