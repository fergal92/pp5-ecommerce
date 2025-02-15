from django.shortcuts import render, redirect
from django.http import HttpResponse

# Newsletter signup view
def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Process the email here (e.g., save it to a database or send a confirmation)
        
        # Redirect the user back to the home page after successful signup
        return redirect('home')  # Replace 'home' with the actual name of your home page URL
    return redirect('home')  # If it's a GET request, redirect to the home page as well
