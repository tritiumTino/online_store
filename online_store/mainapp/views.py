from django.shortcuts import render


def products(request):
    title = 'Продукты'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    slider_products = (
        {'img': 'online_store/img/controll.jpg', 'text': ''},
        {'img': 'online_store/img/controll1.jpg', 'text': ''},
        {'img': 'online_store/img/controll2.jpg', 'text': ''}
    )
    description_list = (
        'Расположитесь комфортно.',
        'Отличное качество материалов позволит вам это.',
        'Различные цвета',
        'высочайший уровень эргономики и прочность.'
    )
    context = {
        'title': title,
        'links_menu': links_menu,
        'slider_products': slider_products,
        'description_list': description_list
    }
    return render(request, 'mainapp/products.html', context=context)
