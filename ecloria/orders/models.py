from django.conf import settings
from django.db import models
from catalog.models import Product


# Order 
""" 
- User
- Product 
- Quantity
- Ordered or Not 
"""
class Order(models.Model):
    # Link each order to a user (customer).
    # If the user is deleted, their orders are also deleted.
    # related_name="orders" lets you access a user's orders via user.orders.all()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    # Link each order to a product.
    # If the product is deleted, related orders will also be deleted.
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    # Number of units of the product in this order.
    quantity = models.IntegerField(default=1)

    # Indicates whether the order has been completed/placed.
    ordered = models.BooleanField(default=False)

    # Store the date and time when the order was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Store the date and time when the order was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the order, useful in the Django admin.
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


# Cart # panier 

""" 
- User
- Order 
- Ordered or Not
- purchase date
"""
# panier

class Cart(models.Model):
    # Link the cart to a single user (each user has only one cart)
    # If the user is deleted, the cart is also deleted
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    # Link the cart to multiple orders
    # A cart can contain multiple orders, and each order can belong to multiple carts (if needed)
    orders = models.ManyToManyField(Order)

    # Indicates whether the cart has been purchased or not
    ordered = models.BooleanField(default=False)

    # Purchase date, can be blank/null if the cart hasn't been purchased yet
    purchase_date = models.DateTimeField(blank=True, null=True)
    
    # String representation of the cart
    # Displays the username of the cart owner in Django admin or when printed
    def __str__(self):
        return self.user.username
