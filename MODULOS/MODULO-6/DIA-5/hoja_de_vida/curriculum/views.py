from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hola(req):
    return HttpResponse("INICIO APP")

def hola_text(req):
    return HttpResponse("Bienvenidos")

def hola_json(req):
    data = {
        "message": "HULK!!!"
    }
    return JsonResponse(data)

def hola_template(req):
    context = {
        "message": "Bienvenidos a utilizar un template dinámico!!!"
    }
    return render(req, 'index.html', context)


# render -> template
# HttpResponse -> text
# JsonResponse -> json