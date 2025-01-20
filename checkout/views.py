from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Qj6tXP5IE40WJpPxU9mqYdRUu3czhMfrz5LZgTHQOLEQtOcdjB2Wq5RB99uJkmqYQXeAyB7kMv0NhAGUrUuTXcV00w9KUDH6g',
        'client_secret':'sk_test_51Qj6tXP5IE40WJpPhGPQSvHEtbacFUmDRHCXKqcTBrH0qnEXKfIl2VO1l9r4yZIqpOmIIW5MjFNv2lrDhlAAzoLm00vM4Xm8Ye',
    }

    return render(request, template, context)