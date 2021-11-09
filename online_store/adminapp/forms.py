from django import forms
from authnapp.forms import ShopUserEditForm
from authnapp.models import ShopUser
from mainapp.models import Category, Product


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ShopUserAdminEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in ('is_active', 'is_superuser', 'is_staff'):
                field.widget.attrs['class'] = 'form-check-input'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description', 'is_active')

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_active':
                field.widget.attrs['class'] = 'form-check-input'


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_active':
                field.widget.attrs['class'] = 'form-check-input'
