from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name="add-to-cart"),
    path('cart/', views.cart, name="cart"),
    
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
