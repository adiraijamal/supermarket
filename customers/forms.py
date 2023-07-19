from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    door_no = forms.CharField(label='Door Number')
    street = forms.CharField(label='Street')
    city = forms.CharField(label='City')
    pincode = forms.CharField(label='Pincode')
    state = forms.CharField(label='State')
    country = forms.CharField(label='Country')

    class Meta:
        model = Customer
        fields = ['fname', 'lname', 'phone_number', 'loyalty_points', 'door_no', 'street', 'city', 'pincode', 'state', 'country']
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'phone_number': 'Phone Number',
            'loyalty_points': 'Loyalty Points',
            'door_no': 'Door Number',
            'street': 'Street',
            'city': 'City',
            'pincode': 'Pincode', 
            'state': 'State',
            'country': 'Country',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['loyalty_points'].widget.attrs['readonly'] = True

    def clean(self):
        cleaned_data = super().clean()
        door_no = cleaned_data.get('door_no')
        street = cleaned_data.get('street')
        city = cleaned_data.get('city')
        pincode = cleaned_data.get('pincode')
        state = cleaned_data.get('state')
        country = cleaned_data.get('country')
        cleaned_data['address'] = f"{door_no}, {street}, {city}, {state}, {country}"
        return cleaned_data
