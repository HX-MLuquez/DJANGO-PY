from django.shortcuts import render

# Create your views here.
def home(req):
    context = {
        "message": "Bienvenidos a ONLY-FLANS",
    }
    return render(req, 'index.html', context)

def acerca(req):
    return render(req, 'about.html', {})