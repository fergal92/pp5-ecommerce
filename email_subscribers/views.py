# views.py
from django.shortcuts import render, redirect
from .models import NewsletterSubscription  # Import the model
from django.contrib import messages


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
