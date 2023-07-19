from django import forms
from .models import Purchase
from products.models import Product
from vendors.models import Vendor


class PurchaseForm(forms.ModelForm):
    product = forms.ChoiceField(
        choices=[('', '---------')] + list(Product.objects.values_list('id', 'name')),
        label='Product',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    vendor = forms.ChoiceField(
        choices=[('', '---------')] + list(Vendor.objects.values_list('id', 'name')),
        label='Vendor',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cashier = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Purchase
        fields = ['cashier', 'product', 'vendor', 'purchase_date', 'cost_price', 'quantity']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['cashier'].widget = forms.HiddenInput()  # Hide the cashier field
        self.fields['product'].choices = [('', '---------')] + list(Product.objects.values_list('id', 'name'))
        self.fields['vendor'].choices = [('', '---------')] + list(Vendor.objects.values_list('id', 'name'))

    def save(self, commit=True):
        if self.request and self.request.user:
            self.instance.cashier = self.request.user
        self.instance.product = Product.objects.get(pk=self.cleaned_data['product'])
        self.instance.vendor = Vendor.objects.get(pk=self.cleaned_data['vendor'])
        return super().save(commit=commit)

