from django.urls import path

from . import views 

urlpatterns = [
    path('', views.hola),
    path('text/', views.hola_text),
    path('json/', views.hola_json),
    path('template/', views.hola_template),
]