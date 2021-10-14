from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login(request):
    title = 'вход'

    if request.method != 'POST':
        form = ShopUserLoginForm()
    else:
        form = ShopUserLoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('index')
    context = {
        'login_form': form,
        'title': title
    }
    return render(request, 'authnapp/account/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'register_form': register_form
    }

    return render(request, 'authnapp/account/register.html', context)


@login_required
def edit(request):
    title = 'профиль'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'title': title,
        'edit_form': edit_form
    }

    return render(request, 'authnapp/edit.html', context)
