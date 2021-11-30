from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from basketapp.models import Basket
from random import sample
from django.conf import settings
from django.core.cache import cache


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(slug):
    if settings.LOW_CACHE:
        key = f'product_{slug}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, slug=slug)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, slug=slug)


def get_related_products(product):
    related_products = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id)[:3]
    return related_products


def get_hot_product():
    products = get_products()
    return sample(list(products), 1)[0]


def products(request, page=1):
    title = 'Продукты'
    product_list = Product.objects.filter(is_active=True)
    paginator = Paginator(product_list, 4)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'products': products_paginator,
        'hot_product': get_hot_product(),
    }
    return render(request, 'mainapp/products.html', context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug__iexact=slug, is_active=True)
    title = category.name
    products = category.products.filter(is_active=True)
    context = {
        'category': category,
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/category.html', context=context)


def product_detail(request, slug):
    product = get_product(slug)
    title = product.name
    context = {
        'product': product,
        'title': title,
        'related_products': get_related_products(product),
    }
    return render(request, 'mainapp/product.html', context=context)
