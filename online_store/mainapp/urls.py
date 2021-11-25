from django.urls import path
from .views import products, category_detail, product_detail

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='main'),
    path('page/<int:page>/', products, name='products'),
    path('category/<str:slug>/', category_detail, name='category_detail'),
    path('product/<str:slug>/', product_detail, name='product_detail'),
]
