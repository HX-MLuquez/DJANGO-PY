from django.shortcuts import render

# Create your views here.
def home(req):
    url = "https://www.recetasnestle.com.ar/sites/default/files/styles/recipe_detail_desktop/public/srh_recipes/919838d8da6d04b4cfaa1b121eeddce2.jpg"
    context = {
        "message": "Bienvenidos a ONLY-FLANS",
        # "products": ["img/OnlyFlans.png", "img/bg-hero.jpg", "img/flans.png"],
         "urls": ["https://blog.pizcadesabor.com/wp-content/uploads/2012/11/empanadas-12.jpg","https://thatovenfeelin.com/wp-content/uploads/2024/01/EASY-PINEAPPLE-DESSERT-1.png", "https://supersisterfitness.com/wp-content/uploads/2013/11/pumpkinpie-1024x10241.jpg"],
         "user": {"username": "Toto", "password": 1234, "is_active": False},
        "productos": [{"name": "tv", "url":url, "descripcion": "hola"},{"name": "celu", "url":url, "descripcion": "hola"},{"name": "mesa", "url":url, "descripcion": "hola"},{"name": "silla", "url":url, "descripcion": "hola"},{"name": "tabla", "url":url, "descripcion": "hola"}, {"name": "pared", "url":url, "descripcion": "hola"}]
    }
    return render(req, 'webtemp/index.html', context)

def acerca(req):
    contex = {
        "data": ""
    }
    return render(req, 'webtemp/about.html', contex)


# nombre = "'Mau'" # 'Mau'
# nombre = "Mau" # Mau