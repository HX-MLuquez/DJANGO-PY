from django.shortcuts import render
from .models import Flan

# Create your views here.
def home(req):
    flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(req, 'webtemp/index.html', {"flanes_publicos": flanes_publicos})


def acerca(req):
    contex = {
        "data": ""
    }
    return render(req, 'webtemp/about.html', contex)


# nombre = "'Mau'" # 'Mau'
# nombre = "Mau" # Mau