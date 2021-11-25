from django.core.management.base import BaseCommand
from mainapp.models import Category, Product, Contact
from authnapp.models import ShopUser
from django.contrib.auth.models import User

import json
import os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding="utf-8") as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = load_from_json('categories')

        Category.objects.all().delete()
        for category in categories:
            Category.objects.create(**category)

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            Product.objects.create(**product)

        contacts = load_from_json('contacts')
        Contact.objects.all().delete()
        for contact in contacts:
            Contact.objects.create(**contact)

        super_user = ShopUser.objects.create_superuser('tritium', 'tinotiano@gmail.com', '1111', age=33)
