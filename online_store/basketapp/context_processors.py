from basketapp.models import Basket


def basket(request):
    print(f'context processor basket works')
    basket = []
    total = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        if basket:
            total = list(basket)[0].get_total_quantity
    return {
        'basket': basket,
        'total': total
    }
