# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    # Champs supplémentaires
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=30, required=True, label="Nom de famille")

    class Meta:
        model = User
        # Ordre et champs affichés dans le formulaire
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
        labels = {
            'username' : "Nom d'utilisateur",
            'password1': "Mot de passe",
            'password2': "Confirmer le mot de passe"
        }
    def save(self, commit=True):
        # Sauvegarde personnalisée
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data.get("first_name", "")
        user.last_name = self.cleaned_data.get("last_name", "")
        if commit:
            user.save()
        return user
