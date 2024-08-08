from django.shortcuts import render

# Create your views here.

def inicio(req): 
    context = {
        "mensaje": "APP WEBZ",
        "productos": [{"name": "tv", "url":"vvv"},{"name": "celu", "url":"www"},{"name": "mesa", "url":"zzz"}]
    }
    return render(req, 'webztemp/index.html', context)

#! 'webz/index.html' <- necesario al usar varias apps que usan templates de igual nombre

def acerca(req): 
    context = {
        "mensaje": "Soy un dev que ...",
    }
    return render(req, 'webztemp/acerca.html', context)

def detalle(req): 
    return render(req, 'webztemp/detalle_producto.html', {})