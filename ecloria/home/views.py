from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté
        print(f"Utilisateur connecté : {request.user.username}")
    else:
        # L'utilisateur n'est pas connecté
        print("Utilisateur non connecté")
    return render(request, "home/home.html")
