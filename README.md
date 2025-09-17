##  Ecloria - Site E-commerce avec Django & Stripe

Un projet Django permettant de gérer un catalogue de produits avec images, un panier d’achats, et un paiement en ligne avec Stripe (mode test).  
Projet développé avec **Poetry** pour la gestion des dépendances.

---

##  Fonctionnalités principales

-  Authentification utilisateur (connexion / inscription)
-  Espace **superadmin** (via Django Admin)
-  Catalogue de produits (nom, prix, description, image avec **Pillow**)
-  Ajout d’un produit au panier
-  Gestion du panier :
  - Afficher le contenu
  - Modifier les quantités
  - Supprimer un produit
  - Vider tout le panier
-  Paiement sécurisé via **Stripe Checkout** (mode test)
-  Page de succès et page d’annulation après paiement

---

##  Installation et configuration

### 1. Cloner le projet
```bash
git clone https://github.com/mon-compte/ecloria.git
cd ecloria

### 2. Installer Poetry
pip install poetry

### 3. Installer les dépendances avec Poetry
poetry install

### 4. Activer l’environnement virtuel
poetry env activate

### 5. Configurer les variables d’environnement
Créer un fichier .env à la racine du projet avec tes clés Stripe (mode test) 

### 6. Appliquer les migrations
python manage.py migrate

### 7. Créer un superutilisateur
python manage.py createsuperuser

### 8. Lancer le serveur
python manage.py runserver
