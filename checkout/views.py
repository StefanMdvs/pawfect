from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.context import bag_contents

import stripe

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oups! Looks like your\
            bag is empty at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KItbaCAfzfv0CFsZfGYC76bW1aFfiKdOXCvv9TQL4j1GREojNsJwJFjpUVZRiudb9ZDVxUTbDecpRcPNP256Eg200ASKaCe9X',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
