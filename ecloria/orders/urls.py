from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('product/<str:slug>/add-to-cart', views.add_to_cart, name="add-to-cart")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)