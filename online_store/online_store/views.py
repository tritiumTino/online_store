from django.shortcuts import render
from mainapp.models import Product, Contact


def index(request):
    title = 'магазин'
    products = Product.objects.all()[:4]
    context = {
        'title': title,
        'products': products
    }

    return render(request, 'online_store/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    contact_list = Contact.objects.all()
    context = {
        'title': title,
        'contacts': contact_list
    }
    return render(request, 'online_store/contact.html', context=context)
