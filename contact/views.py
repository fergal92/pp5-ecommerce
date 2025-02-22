# contact/views.py
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data and send an email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email (you need to configure your email backend in settings.py)
            send_mail(
                f"Message from {name}",
                message,
                email,
                [settings.CONTACT_EMAIL],  # This should be your email
            )
            # Redirect to a 'success' page
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

# contact/views.py
def thanks_view(request):
    return render(request, 'contact/thanks.html')

