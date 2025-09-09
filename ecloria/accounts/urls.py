# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL pour la page d'inscription
    path("signup/", views.signup_view, name="signup"),

    # URL pour la page de connexion
    path("login/", views.login_view, name="login"),

    # URL pour la déconnexion
    path("logout/", views.logout_view, name="logout"),
]
