from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name="add-to-cart"),
    path('cart/', views.cart, name="cart"),
    path('cart/delete/', views.delete_cart, name="delete-cart"), # Supprime tout le panier
    path('cart/delete/<int:order_id>/', views.delete_order, name="delete-order"),  # supprime un produit
    path('cart/update/<int:order_id>/', views.update_quantity, name="update-quantity"),  # changer la quantité
     # Stripe Checkout
    path('create-checkout-session/', views.create_checkout_session, name="create-checkout-session"),
    path('success/', views.checkout_success, name='checkout-success'),
    path('cancel/', views.checkout_cancel, name='checkout-cancel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # Route pour ajouter un produit au panier
#     path('product/<int:product_id>/add-to-cart/', views.add_to_cart, name="add-to-cart"),
# ]

# # Sert à servir les fichiers médias (images) en mode DEBUG
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
