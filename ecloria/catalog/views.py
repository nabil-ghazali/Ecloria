from django.shortcuts import render

def catalog(request):
    return render(request, "catalog/product_list.html")
