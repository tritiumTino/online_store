from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from authnapp.models import ShopUser
from mainapp.models import Category, Product
from authnapp.forms import ShopUserRegisterForm
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from .forms import ShopUserAdminEditForm, CategoryCreateForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'администратор: пользователи'
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи: создать пользователя'
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('staff:users'))

    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи: обновить данные пользователя'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('staff:user_update', args=[pk]))
    else:
        user_form = ShopUserAdminEditForm(instance=user)

    context = {
        'title': title,
        'user_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи: удалить пользователя'
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('staff:users'))

    context = {
        'title': title,
        'user_to_delete': user
    }

    return render(request, 'adminapp/user_delete.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'администратор: категории'
    category_list = Category.objects.all()
    context = {
        'title': title,
        'objects': category_list
    }

    return render(request, 'adminapp/categories.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории: создать новую категорию'
    if request.method == 'POST':
        category_form = CategoryCreateForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('staff:categories'))

    else:
        category_form = CategoryCreateForm()

    context = {
        'title': title,
        'category_form': category_form
    }

    return render(request, 'adminapp/category_update.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории: обновить данные категории'
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category_form = CategoryCreateForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('staff:category_update', args=[pk]))
    else:
        category_form = CategoryCreateForm(instance=category)

    context = {
        'title': title,
        'category_form': category_form
    }

    return render(request, 'adminapp/category_update.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории: удалить категорию'
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()

    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('staff:categories'))

    context = {
        'title': title,
        'category_to_delete': category,
        'products': products,
    }

    return render(request, 'adminapp/category_delete.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def products(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_read(request):
    pass
