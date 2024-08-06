from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(req):
    context = {
        "message": "Bienvenidos a ONLY-FLANS",
        "user": "Manolo",
        "is_active": True
    }
    return render(req, 'index.html', context)


# render -> template
# HttpResponse -> text
# JsonResponse -> json