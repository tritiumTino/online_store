from django.shortcuts import render
from .models import Category, Product


def products(request):
    title = 'Продукты'
    links_menu = Category.objects.all()
    product_list = Product.objects.all()
    slider_products = (
        {'img': 'online_store/img/controll.jpg', 'text': ''},
        {'img': 'online_store/img/controll1.jpg', 'text': ''},
        {'img': 'online_store/img/controll2.jpg', 'text': ''}
    )

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': product_list,
        'slider_products': slider_products,
    }
    return render(request, 'mainapp/products.html', context=context)


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    title = category.name
    links_menu = Category.objects.all()
    products = category.products.all()
    context = {
        'category': category,
        'links_menu': links_menu,
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/category.html', context=context)


def product_detail(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    title = product.name
    context = {
        'product': product,
        'title': title
    }
    return render(request, 'mainapp/product.html', context=context)
