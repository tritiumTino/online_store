from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    title = 'корзина'
    user_basket = Basket.objects.filter(user=request.user)
    context = {
        'basket': user_basket,
        'title': title
    }
    return render(request, 'basketapp/basket.html', context)


def basket_add(request, slug):
    product = get_object_or_404(Product, slug__iexact=slug)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, slug):
    context = {}
    return render(request, 'basketapp/basket.html', context)
