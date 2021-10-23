from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
from random import sample


def get_related_products(product):
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]
    return related_products


def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]


def products(request):
    title = 'Продукты'
    product_list = Product.objects.all()
    context = {
        'title': title,
        'products': product_list,
        'hot_product': get_hot_product()
    }
    return render(request, 'mainapp/products.html', context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug__iexact=slug)
    title = category.name
    products = category.products.all()
    context = {
        'category': category,
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/category.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug__iexact=slug)
    title = product.name
    context = {
        'product': product,
        'title': title,
        'related_products': get_related_products(product),
    }
    return render(request, 'mainapp/product.html', context=context)
