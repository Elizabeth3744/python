from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.inicio),
    path('inicio/', views. plantilla_inicio),
]