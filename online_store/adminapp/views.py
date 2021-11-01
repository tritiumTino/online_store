from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from authnapp.models import ShopUser
from mainapp.models import Category, Product
from authnapp.forms import ShopUserRegisterForm
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from .forms import ShopUserAdminEditForm, CategoryCreateForm, ProductEditForm


class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'
        return context

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('staff:users')


class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('staff:users')


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('staff:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'adminapp/categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['title'] = 'администратор: категории'
        return context

    def get_queryset(self):
        return Category.objects.all().order_by('-is_active',)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    models = Category
    form_class = CategoryCreateForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context['title'] = 'категории: создать новую категорию'
        return context


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('staff:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data()
        context['title'] = 'категории: обновить данные категории'
        return context


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('staff:categories')
    template_name = 'adminapp/category_confirm_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data()
        context['title'] = 'категории: удалить категорию'
        context['products'] = context['object'].products.all()
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    category = Category.objects.get(pk=pk)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'adminapp/products.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукт: создать новый продукт'
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('staff:products', args=[pk]))

    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'product_form': product_form,
        'category': category
    }

    return render(request, 'adminapp/product_update.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'продукт: обновить данные продукта'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product_form = CategoryCreateForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('staff:product_update', args=[pk]))
    else:
        product_form = ProductEditForm(instance=product)

    context = {
        'title': title,
        'product_form': product_form
    }

    return render(request, 'adminapp/product_update.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    title = 'продукт: удалить продукт'
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('staff:products', args=[product.category.pk]))

    context = {
        'title': title,
        'product_to_delete': product,
    }

    return render(request, 'adminapp/product_delete.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    title = 'продукт: подробная информация'
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': title,
        'product': product
    }
    return render(request, 'adminapp/product_read.html', context=context)
