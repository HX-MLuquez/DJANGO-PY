"""
URL configuration for hoja_de_vida project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#* Sin Modularizar las ROUTES
# from django.contrib import admin
# from django.urls import path
# from curriculum.views import hola_text, hola_json, hola_template

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('text/', hola_text),
#     path('json/', hola_json),
#     path('template/', hola_template),
# ]


#* MODULARIZANDO ROUTES
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('curriculum.urls')),
   # path('blog/', include('blog.urls')),
]