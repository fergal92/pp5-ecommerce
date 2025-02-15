from django.urls import path
from . import views  # Make sure this line is included to import your views

urlpatterns = [
    # Other URLs
    path('email_subscribers/', views.newsletter_signup, name='newsletter_signup'),
]
