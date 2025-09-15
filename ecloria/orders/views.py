# orders/views.py

from django.shortcuts import get_object_or_404, redirect, render
from catalog.models import Product
from .models import Cart, Order
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
from django.urls import reverse


# ------------------------- VUES PANIER ------------------------- #

@login_required
def add_to_cart(request, slug):
    """
    Ajouter un produit au panier.
    
    Étapes :
    1. Récupère le produit avec son slug (ou erreur 404 s’il n’existe pas).
    2. Récupère ou crée un panier pour l’utilisateur connecté.
    3. Vérifie si ce produit existe déjà dans une commande (Order) du panier :
       - Si non → crée une commande et l’ajoute au panier.
       - Si oui → incrémente la quantité.
    4. Redirige vers la page détail du produit.
    """
    if request.method == "POST":
        user = request.user
        product = get_object_or_404(Product, slug=slug)

        cart, _ = Cart.objects.get_or_create(user=user)  # crée un panier si inexistant
        order, created = Order.objects.get_or_create(user=user, product=product)

        if created:
            # première fois qu’on ajoute ce produit au panier
            cart.orders.add(order)
            cart.save()
        else:
            # si déjà dans le panier, on augmente la quantité
            order.quantity += 1
            order.save()

    return redirect('product_detail', slug=slug)


@login_required
def cart(request):
    """
    Affiche le contenu du panier de l’utilisateur connecté.
    - Récupère son panier.
    - Passe toutes les commandes associées au template.
    """
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'orders/orders_summary.html', context={"orders": cart.orders.all()})


@login_required
def delete_cart(request):
    """
    Supprime le panier ENTIER de l’utilisateur.
    - Supprime toutes les commandes du panier.
    - Supprime le panier lui-même.
    - Redirige vers l’accueil.
    """
    try:
        cart = Cart.objects.get(user=request.user)
        cart.orders.all().delete()
        cart.delete()
    except Cart.DoesNotExist:
        pass  # si l’utilisateur n’a pas encore de panier

    return redirect('home')  # ⚠️ tu pourrais changer vers une catégorie spécifique


@login_required
def delete_order(request, order_id):
    """
    Supprime un PRODUIT précis du panier.
    - On identifie la commande par son id et l’utilisateur.
    - Si elle existe → on la supprime.
    """
    try:
        order = Order.objects.get(id=order_id, user=request.user)
        order.delete()
    except Order.DoesNotExist:
        pass

    return redirect('cart')


@login_required
def update_quantity(request, order_id):
    """
    Met à jour la quantité d’un produit du panier.
    - Si la nouvelle quantité > 0 → on met à jour.
    - Si la quantité = 0 → on supprime la commande.
    - Si mauvaise valeur (texte, vide, etc.) → on ignore.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == "POST":
        try:
            new_quantity = int(request.POST.get("quantity", 1))
            if new_quantity > 0:
                order.quantity = new_quantity
                order.save()
            else:
                order.delete()
        except ValueError:
            pass  # si input invalide

    return redirect("cart")


# ------------------------- STRIPE CHECKOUT ------------------------- #

# Configuration de Stripe : clé secrète stockée dans .env et importée via settings.py
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def create_checkout_session(request):
    """
    Lance une session de paiement avec Stripe Checkout.
    
    Étapes :
    1. Récupère le panier de l’utilisateur.
    2. Prépare les articles pour Stripe (nom, prix en centimes, quantité).
    3. Crée une session Stripe Checkout avec :
       - les articles
       - le mode paiement (card)
       - l’URL de succès (retour après paiement validé)
       - l’URL d’annulation
    4. Redirige l’utilisateur vers Stripe.
    """
    cart = get_object_or_404(Cart, user=request.user)

    # Liste des produits envoyés à Stripe
    line_items = []
    for order in cart.orders.all():
        line_items.append({
            'price_data': {
                'currency': 'eur',
                'product_data': {'name': order.product.name},
                'unit_amount': int(order.product.price * 100),  # en centimes
            },
            'quantity': order.quantity,
        })

    # Création de la session Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(reverse('home')) + "?success=true",
        cancel_url=request.build_absolute_uri(reverse('cart')),
    )

    return redirect(session.url, code=303)


def checkout_success(request):
    """
    Page affichée après un paiement réussi.
    """
    return render(request, 'orders/checkout_success.html')


def checkout_cancel(request):
    """
    Page affichée si l’utilisateur annule le paiement.
    """
    return render(request, 'orders/checkout_cancel.html')
