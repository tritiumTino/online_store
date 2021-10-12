from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
