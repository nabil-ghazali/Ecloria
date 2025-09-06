from django.urls import path
from .views import catalog

urlpatterns = [
    path('/', catalog, name='categories'),
]
