from django.urls import path
from .views import *


app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='view'),
    path('add/<str:slug>/', basket_add, name='add'),
    path('remove/<str:slug>)/', basket_remove, name='remove'),
]
