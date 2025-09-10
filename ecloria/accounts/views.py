from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm


def signup_view(request):
    """
    Vue pour l'inscription des utilisateurs.

    - Affiche le formulaire d'inscription pour les requêtes GET.
    - Traite le formulaire et crée un nouvel utilisateur pour les requêtes POST.
    - Ajoute un message flash de succès après l'inscription.
    - Ne connecte pas automatiquement l'utilisateur (modifiable si besoin).

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponse: Rend le template 'accounts/signup.html' avec le formulaire et éventuellement les messages.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Création de l'utilisateur dans la base
            messages.success(request, "Inscription réussie, bienvenue !")
            # On peut décider ici si on connecte automatiquement ou non - login(request, user)
            return render(
                request,
                "accounts/signup.html",
                {"form": form, "redirect": True, "messages": messages.get_messages(request)}
            )
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    """
    Vue pour la connexion des utilisateurs.

    - Affiche le formulaire de connexion pour les requêtes GET.
    - Authentifie et connecte l'utilisateur pour les requêtes POST.
    - Ajoute un message flash de succès après la connexion.

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponse: Rend le template 'accounts/login.html' avec le formulaire et éventuellement les messages.
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Connexion de l'utilisateur
            messages.success(request, "Connexion réussie !")
            return render(request, "accounts/login.html", {"form": form, "redirect": True})
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    """
    Vue pour la déconnexion des utilisateurs.

    - Déconnecte l'utilisateur actuel.
    - Ajoute un message flash de succès.
    - Redirige vers la page d'accueil.

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponseRedirect: Redirection vers la page 'home'.
    """
    logout(request)  # Déconnexion de l'utilisateur
    messages.success(request, "Déconnexion réussie !")
    return redirect("home")
