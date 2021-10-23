from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from PIL import Image
from phone_field import PhoneField


_MAX_SIZE = 270


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True, verbose_name='название')
    description = models.TextField(verbose_name='описание', blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name='ссылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    is_active = models.BooleanField(verbose_name='активно', default=True)

    def get_absolute_url(self):
        return reverse('products:category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        if self.is_active is False:
            for product in self.products.all():
                product.is_active = False
                product.save()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name', '-created_at')


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', related_name='products')
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name='ссылка')
    image = models.ImageField(upload_to='media/products_images/%Y', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    is_active = models.BooleanField(verbose_name='активно', default=True)

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = f'{gen_slug(self.name)}-{int(time())}'
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > _MAX_SIZE or img.width > _MAX_SIZE:
            img = img.resize(
                (_MAX_SIZE, _MAX_SIZE),
                Image.ANTIALIAS
            )
            img.save(self.image.path)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('-created_at',)


class Contact(models.Model):
    city = models.CharField(max_length=128, verbose_name='город')
    tel = PhoneField(blank=True, help_text='+79999999999', verbose_name='Телефон')
    email = models.EmailField(max_length=254, verbose_name='email')
    address = models.CharField(max_length=256, verbose_name='адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('-updated_at', )
