from django.shortcuts import render

# Create your views here.
def home(req):
    context = {
        "message": "Bienvenidos a ONLY-FLANS",
        # "products": ["img/OnlyFlans.png", "img/bg-hero.jpg", "img/flans.png"],
         "urls": ["https://blog.pizcadesabor.com/wp-content/uploads/2012/11/empanadas-12.jpg","https://thatovenfeelin.com/wp-content/uploads/2024/01/EASY-PINEAPPLE-DESSERT-1.png", "https://supersisterfitness.com/wp-content/uploads/2013/11/pumpkinpie-1024x10241.jpg"],
         "user": {"username": "Toto", "password": 1234, "is_active": False},
        "productos": [{"name": "tv", "url":"vvv"},{"name": "celu", "url":"vvv"},{"name": "mesa", "url":"vvv"}]
    }
    return render(req, 'index.html', context)

def acerca(req):
    contex = {
        "data": ""
    }
    return render(req, 'about.html', contex)