from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser

# Modéle 1 : Création de la classe catégorie des produits
"""
Category
- Nom
- Description
- Résultats (Nombre total de produits dans la category)
- Image

"""

class Category(models.Model):
    names = models.CharField(max_length=200)           
    description = models.TextField(blank=True, null=True)
    results = models.IntegerField(default=0)
    thumbnail = models.ImageField(upload_to='catalogues/', blank=True, null=True)

    def __str__(self):
        return self.names



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='catalogues/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name




