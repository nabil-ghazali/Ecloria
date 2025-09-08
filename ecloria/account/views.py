from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm  # <-- formulaire personnalisé
from django.contrib.auth.forms import  AuthenticationForm

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! Redirection vers la page d'accueil...")
            return render(request, "accounts/signup.html", {"form": form, "redirect": True})
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie ! Redirection vers la page d'accueil...")
            return render(request, "accounts/login.html", {"form": form, "redirect": True})
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Déconnexion réussie !")
        return redirect("home")
