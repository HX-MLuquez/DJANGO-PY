from django.shortcuts import render

# Create your views here.

def inicio(req): 
    context = {
        "mensaje": "APP WEBZ",
        "productos": [{"name": "tv", "url":"vvv"},{"name": "celu", "url":"www"},{"name": "mesa", "url":"zzz"}]
    }
    return render(req, 'index.html', context)

def acerca(req): 
    context = {
        "mensaje": "Soy un dev que ...",
    }
    return render(req, 'acerca.html', context)