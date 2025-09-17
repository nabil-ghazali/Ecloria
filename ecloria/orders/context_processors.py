# orders/context_processors.py
from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user, ordered=False)
            # Somme des quantités de toutes les commandes
            return {"cart_item_count": sum(order.quantity for order in cart.orders.all())}
        except Cart.DoesNotExist:
            return {"cart_item_count": 0}
    return {"cart_item_count": 0}