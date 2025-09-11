
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Page d'accueil
    path('/<int:category_id>/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



