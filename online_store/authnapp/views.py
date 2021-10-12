from django.shortcuts import render, HttpResponseRedirect
from .forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = 'вход'

    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if login_form.is_valid():
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    login_form = ShopUserLoginForm()

    context = {'title': title, 'login_form': login_form}
    return render(request, 'authnapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
