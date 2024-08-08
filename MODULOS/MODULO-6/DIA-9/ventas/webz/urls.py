
from django.urls import path
from . import views

# /z/
urlpatterns = [
    path('', views.inicio),
    path('acerca/', views.acerca),
    path('detalle/', views.detalle)
]
