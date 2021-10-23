from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


def products(request):
    title = 'Продукты'
    links_menu = Category.objects.all()
    product_list = Product.objects.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': product_list,
    }
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context.update({
            'basket': basket
        })
    return render(request, 'mainapp/products.html', context=context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug__iexact=slug)
    title = category.name
    links_menu = Category.objects.all()
    products = category.products.all()
    context = {
        'category': category,
        'links_menu': links_menu,
        'title': title,
        'products': products
    }
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context.update({
            'basket': basket
        })
    return render(request, 'mainapp/category.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug__iexact=slug)
    title = product.name
    links_menu = Category.objects.all()
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    context = {
        'product': product,
        'title': title,
        'related_products': related_products,
        'links_menu': links_menu
    }
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        context.update({
            'basket': basket
        })
    return render(request, 'mainapp/product.html', context=context)
