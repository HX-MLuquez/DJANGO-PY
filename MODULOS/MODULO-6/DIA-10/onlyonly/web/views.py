from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan
# from .forms import ContactFormForm


def indice(request):
    # public_flans = [{"name": "flan 1", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 1"}, {"name": "flan 2",                                                                                                                              "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 2"}, {"name": "flan 3", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 3"}]
    # return render(request,'index.html',{'public_flans': public_flans})

    # flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        "mensaje": "hola",
        "flanes_publicos": flanes_publicos
    }
    return render(request, 'index.html', context)


def acerca(request):
    # *  <!-- apply filtros -->
    return render(request, 'about.html', {})


def bienvenido(request):
    # private_flans = [{"name": "flan 7", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 7"},
    #                  {"name": "flan 8", "image_url": "https://pbs.twimg.com/media/CA5u_1pWYAE6FK0.jpg", "description": "flan 8"},]
    # return render(request,'welcome.html',{'private_flans': private_flans})
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {"private_flans": private_flans})

# *  <!-- apply FORM contacto -->


def contacto(request):
    return render(request, 'contactus.html', {})


# *  --- apply ContactModelForm ---
# from .forms import ContactModelForm  # Asegúrate de importar el formulario correcto

# *  <!-- apply MODEL-FORM contacto -->
def contacto_model_form(request):
    return render(request, 'contactus_model_form.html', {})
# *  --- apply ContactModelForm ---


# * <!-- apply DAY 11 - 12 -->
def exito(request):
    return render(request, 'success.html', {})
