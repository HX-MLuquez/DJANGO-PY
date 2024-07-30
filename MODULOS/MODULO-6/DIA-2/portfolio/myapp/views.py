from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola_mundo(req):
    return HttpResponse("Hola Mundo!!!")

def bye_mundo(req):
    return HttpResponse("BYE BYE BYE!!!")

def part_html(req):
    return HttpResponse("<h1>HOLA SOY UN H1 MUNDO!!!</h1>")
