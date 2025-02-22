# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", required=True)
    email = forms.EmailField(label="Your Email", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Your Message", required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError("Please enter a valid email address.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message should be at least 10 characters.")
        return message
