from django.shortcuts import render
from mainapp.models import Product, Contact
from basketapp.models import Basket


def index(request):
    title = 'магазин'
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products,
    }
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context.update({
            'basket': basket
        })

    return render(request, 'online_store/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    contact_list = Contact.objects.all()
    context = {
        'title': title,
        'contacts': contact_list,
    }
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context.update({
            'basket': basket
        })
    return render(request, 'online_store/contact.html', context=context)
