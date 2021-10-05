from django.shortcuts import render


def index(request):
    title = 'магазин'
    context = {
        'title': title,
    }
    return render(request, 'online_store/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    contact_list = (
        {'city': 'Москва', 'tel': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        {'city': 'Москва', 'tel': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        {'city': 'Москва', 'tel': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'}
    )
    context = {
        'title': title,
        'contacts': contact_list
    }
    return render(request, 'online_store/contact.html', context=context)
