Dossier/App	Rôle
ecloria/	Le projet principal (configuration globale, routes, settings)
users/	Gestion des utilisateurs et rôles (client/admin)
catalog/	Gestion des produits et catégories
orders/	Gestion des commandes et paiements
templates/	Pages HTML que l’utilisateur voit
static/	Fichiers CSS, JS et images pour le site
media/	Fichiers uploadés par les utilisateurs (photos produits, avatars…)
tests/	Tests pour vérifier que tout fonctionne correctement


ecloria/                  # Racine du projet
├── .gitignore
├── pyproject.toml
├── poetry.lock
├── README.md
├── .env.example
├── manage.py
├── ecloria/               # Projet Django principal
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── home/                  # App pour la page d'accueil
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── views.py           # Vue home
│   ├── urls.py            # URL de la page d'accueil
│   └── migrations/
├── users/                 # App utilisateurs
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── catalog/               # App produits et catégories
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── orders/                # App commandes et paiements
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── templates/             # Templates HTML
│   ├── base.html          # Layout global
│   ├── home/
│   │   └── home.html      # Page d'accueil
│   ├── users/
│   │   └── login.html
│   ├── catalog/
│   │   ├── product_list.html
│   │   └── product_detail.html
│   └── orders/
│       └── order_summary.html
├── static/                # Fichiers CSS, JS, images
│   ├── css/
│   │   └── base.css
│   ├── js/
│   │   └── script.js
│   └── img/
├── media/                 # Fichiers uploadés
└── tests/                 # Tests unitaires
    ├── __init__.py
    ├── test_home.py
    ├── test_users.py
    ├── test_catalog.py
    └── test_orders.py
