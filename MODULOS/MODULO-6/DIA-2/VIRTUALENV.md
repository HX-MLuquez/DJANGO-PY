
1. Verificar si ya está en nuestro sistema
```bash
virtualenv --version
```

2. Instalar
```bash
pip install virtualenv
```
```bash
virtualenv --version
```

3. Crear Entorno Virtual
```bash
virtualenv venv
```

4. Conectarnos a nuestro entorno virtual - ACTIVATE
```bash
source venv/Scripts/activate
```

---

Comandos de Consulta de Dependencias Instaladas
```bash
pip list
```
```bash
pip freeze
```



---

## PROYECTO con DJANGO
1. Instalar Django
```bash
pip install django
```
**para DESINSTALAR**
```bash
pip uninstall django
```

2. Verificar
```bash
django-admin --version
```

3. Crear proyecto
```bash
django-admin startproject portfolio .
```

4. Levantar nuestro SERVER (nuestro proyecto)

```bash
python manage.py runserver
```

5. Migramos las tablas que vienen por defecto para el ADMIN de Django
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```



6. HABILITAR Claves del ADMIN
```bash
python manage.py createsuperuser
```

---
**CORTAR SEVER**
ctrl + C


```
```

---

## MODELO crear Entorno Virtual Nativo de PYTHON

```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```

---

# CREAR APP
```bash
python manage.py startapp myapp
```