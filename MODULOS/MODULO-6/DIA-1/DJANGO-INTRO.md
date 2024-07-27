
# DJANGO - PRIMER PROYECTO

Dentro ya de nuestro entorno virtual 

- pip install django
- django-admin --version


## Crear PROYECTO
- django-admin startproject myproject 
- django-admin startproject myproject . 

- python manage.py help

## LEVANTAR SERVER 
- python manage.py runserver

En puerto determinado 3000
- python manage.py runserver 3000


## MIGRATE
- python manage.py makemigrations
- python manage.py migrate




---

Error Kathy
```
$ pip install django
ERROR: Could not install packages due to an OSError: Could not find a suitable TLS CA certificate bundle, invalid path: C:\Program Files\PostgreSQL\16\ssl\certs\ca-bundle.crt

WARNING: There was an error checking the latest version of pip.
(env)

deactivate 
python --version

python -m pip install --upgrade pip
pip --version


python - No se pudieron instalar paquetes debido a un EnvironmentError: No se pudo encontrar un paquete de certificados de CA TLS adecuado, ruta no válida - Desbordamiento de pila (stackoverflow.com)
Variables de entorno <- 
```