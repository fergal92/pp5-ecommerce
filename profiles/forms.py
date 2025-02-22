from django import forms
from .models import UserProfile
import pycountry
from datetime import date, timedelta
from django.core.exceptions import ValidationError


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'border-black rounded-0 profile-form-input',
                'type': 'text',  # Changed from "date" to "text"
                'placeholder': 'Date of Birth',
                # When clicked, change to date picker
                'onfocus': "(this.type='date')",
                # When not in focus, change back to text
                'onblur': "(this.type='text')",
            }
        ),
        label=False,  # Hide label if you only want the placeholder
    )

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_country': 'Country code',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
            'date_of_birth': 'Date of Birth'  # ✅ Ensure this placeholder is set
        }

        # Generate country choices from pycountry
        countries = [(country.alpha_2, country.name)
                    for country in pycountry.countries]
        self.fields['default_country'].choices = [
            ('', 'Select a country')] + countries

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders.get(field, '')
            if self.fields[field].required:
                placeholder += ' *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today - date_of_birth
            if age < timedelta(days=16*365):
                raise ValidationError('You must be at least 16 years old.')
        return date_of_birth
