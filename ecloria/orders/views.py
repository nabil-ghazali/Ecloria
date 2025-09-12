# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from ecloria.catalog.models import Product
from ecloria.orders.models import Cart, Order




def add_to_cart(request, slug):
    # Get the current logged-in user from the request
    user = request.user

    # Try to fetch the product with the given slug, or return 404 if not found
    product = get_object_or_404(Product, slug=slug)

    # Get the cart for this user, or create one if it doesn't exist yet
    cart, _ = Cart.objects.get_or_create(user=user)

    # Try to get an existing order for this user and product,
    # or create a new one if it doesn’t exist
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        # If a new order was created, add it to the cart
        cart.orders.add(order)
        cart.save()
    else:
        # If the order already exists, increase the quantity
        order.quantity += 1
        order.save()

    # Redirect the user back to the product page
    return redirect(reverse("product", kwargs={"slug": slug}))
