# MODELS

1. Crear el Model -> models.py 
2. Register en admin.py
```py
from .models import Flan
# Register your models here.

admin.site.register(Flan)
```
3. python manage.py makemigrations

Se crea un archivo en la carpeta migrations

4. python manage.py migrate

Se crea la Tabla equivalente a nuestro Model

5. Ingresar a la app como admin /admin

6. Ir a la tabla FLAN y crear flanes

7. Buscar data en nuestra db por medio del MODEL
```py
def home(req):
    flanes_all = Flan.objects.all()
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(req, 'webtemp/index.html', {"flanes_publicos": flanes_publicos})
```