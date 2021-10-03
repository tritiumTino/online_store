from django.shortcuts import render


def index(request):
    return render(request, 'online_store/index.html')


def contacts(request):
    return render(request, 'online_store/contact.html')
