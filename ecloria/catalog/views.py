from django.shortcuts import render, get_object_or_404, render
from catalog.models import Category, Product

def home(request):

    catalogues = Category.objects.all()
    return render(request, 'home/home.html', {
        "catalogues": catalogues,
        "categories": catalogues 
    })
    


def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'catalog/list_cat.html', {'categories': categories})




def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'catalog/product_list.html', {
        'category': category,
        'products': products
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'catalog/product_detail.html', {'product': product})
