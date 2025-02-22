# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact_form'),
    path('thanks/', views.thanks_view, name='thanks'),
]
