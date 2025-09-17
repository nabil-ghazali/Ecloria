from django.conf import settings
from django.db import models
from catalog.models import Product


# -------------------------------
# 📦 Order (Commande d’un produit)
# -------------------------------
"""
Un Order représente UNE ligne de commande :
- Quel utilisateur a commandé ?
- Quel produit a été ajouté au panier ?
- Quelle quantité ?
- Est-ce que la commande a été validée (passée) ou non ?
"""
class Order(models.Model):
    # Lien vers l’utilisateur qui a passé la commande
    # settings.AUTH_USER_MODEL = modèle User défini dans ton projet (souvent "auth.User" ou "accounts.User")
    # CASCADE : si un utilisateur est supprimé, toutes ses commandes le sont aussi
    # related_name="orders" → permet d’écrire user.orders.all() pour accéder aux commandes d’un utilisateur
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    # Lien vers le produit commandé
    # CASCADE : si le produit est supprimé, toutes les commandes associées disparaissent aussi
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    # Nombre d’unités du produit commandées
    quantity = models.IntegerField(default=1)

    # Est-ce que cette commande a été validée (payée) ?
    ordered = models.BooleanField(default=False)

    # Date de création de la commande (automatique)
    created_at = models.DateTimeField(auto_now_add=True)

    # Date de dernière modification (mise à jour auto à chaque changement)
    updated_at = models.DateTimeField(auto_now=True)

    # Représentation lisible de l’objet (utile dans l’admin Django et le shell)
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


# -------------------------------
# 🛒 Cart (Panier d’un utilisateur)
# -------------------------------
"""
Un Cart représente le PANIER d’un utilisateur :
- Chaque utilisateur a UN SEUL panier actif
- Un panier peut contenir plusieurs commandes (Order)
- On peut savoir si le panier est validé (payé) ou encore en cours
"""
class Cart(models.Model):
    # Lien unique vers un utilisateur (chaque utilisateur a un panier)
    # OneToOneField → garantit qu’un seul panier par utilisateur existe
    # CASCADE : si l’utilisateur est supprimé, son panier l’est aussi
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    # Relation ManyToMany avec Order → un panier peut contenir plusieurs commandes
    orders = models.ManyToManyField(Order)

    # Indique si le panier a été finalisé (payé) ou pas
    ordered = models.BooleanField(default=False)

    # Date d’achat → reste vide tant que le panier n’a pas été validé
    purchase_date = models.DateTimeField(blank=True, null=True)
    
    # Représentation lisible de l’objet (affiche le nom d’utilisateur)
    def __str__(self):
        return self.user.username
