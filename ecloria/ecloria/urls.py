

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
   path('', include('catalog.urls')),  # page d'accueil
    path('', include('catalog.urls')),  # pas besoin de répéter /category/ ici

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 