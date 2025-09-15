# orders/views.py
from django.shortcuts import get_object_or_404, redirect, render
from catalog.models import Product
from .models import Cart, Order
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, slug):
    if request.method == "POST":
        user = request.user
        product = get_object_or_404(Product, slug=slug)

        cart, _ = Cart.objects.get_or_create(user=user)
        order, created = Order.objects.get_or_create(user=user, product=product)

        if created:
            cart.orders.add(order)
            cart.save()
        else:
            order.quantity += 1
            order.save()

    return redirect('product_detail', slug=slug)

@login_required
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'orders/orders_summary.html', context={"orders":cart.orders.all()})
