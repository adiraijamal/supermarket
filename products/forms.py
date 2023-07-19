# forms.py
from django import forms
from products.models import Product
from vendors.models import Vendor


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choices = [('', '---------')] + list(Vendor.objects.all().values_list('id', 'name'))
        self.fields['vendor'].widget = forms.Select(choices=choices)

    class Meta:
        model = Product
        fields = ['name', 'description', 'vendor', 'cost_price', 'selling_price', 'quantity']
