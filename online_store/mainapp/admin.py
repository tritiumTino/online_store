from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('city', 'tel', 'email', 'address')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
