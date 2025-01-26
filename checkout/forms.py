from django import forms
from .models import Order
import pycountry

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                'street_address1', 'street_address2',
                'town_or_city', 'postcode', 'country',
                'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
                
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country code',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, Sate or Locality',
        }
        

        # Generate country choices from pycountry
        countries = [(country.alpha_2, country.name) for country in pycountry.countries]
        self.fields['country'].choices = [('', 'Select a country')] + countries

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders.get(field, '')
            if self.fields[field].required:
                placeholder += ' *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False