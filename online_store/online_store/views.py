from django.shortcuts import render
from mainapp.models import Product, Contact
from basketapp.models import Basket


def index(request):
    title = 'магазин'
    context = {
        'title': title,
    }
    return render(request, 'online_store/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    contact_list = Contact.objects.all()
    context = {
        'title': title,
        'contacts': contact_list,
    }
    return render(request, 'online_store/contact.html', context=context)
