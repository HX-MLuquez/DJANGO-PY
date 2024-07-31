from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def saludar_function(request):
    return HttpResponse("Hola MUNDO!!!")