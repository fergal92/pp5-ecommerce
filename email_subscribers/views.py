# views.py
from django.shortcuts import render, redirect
from .models import NewsletterSubscription  # Import the model
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Check if the email already exists in the database
            subscription, created = NewsletterSubscription.objects.get_or_create(
                email=email)

            # Show a message to the user based on whether the email was newly
            # added
            if created:
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.info(request, "You are already subscribed!")

            # Redirect to the home page after submission
            return redirect('home')
    return redirect('home')  # If not a POST request, redirect to the home page


def send_verification_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = f"http://{request.get_host()}/verify-email/{uid}/{token}/"
    
    subject = "Verify Your Email"
    message = render_to_string('emails/verification_email.html', {
        'user': user,
        'verification_link': verification_link,
    })
    send_mail(subject, message, 'noreply@yourdomain.com', [user.email])