# HITO 1 - PROYECTO
1. Levantar primer proyecto en Django
  - Utiliza el administrador de paquetes PIP para la instalación de los componentes Django.
  - Crea la carpeta onlyflans
  - Dentro de esta crea un entorno virtual y recuerda de activar
  - Instala Django 5.0.7 y Crea un project con el llamado onlyflans (recuerden usar el punto al final)
    - Ver de instalar mediante django==3.2.4 <- solamente
  - Probar el Proyecto ejecutando runserver
  - Preparar y migrar
  - Crear user y password del admin
  - Probar el Proyecto ejecutando runserver e ingresar como admin
  - Crear una app llamada web
  - Armar la estructura
    - static
        - js
        - css
    - templates
    - etc

  ---
Adicional
  - En la views.py de web crear una función de respuesta http 
  - En la urls.py del proyecto anexar la route para la función previamente creada
  - Modularizar la route creada (utilizando el include)
  - Utiliza el utilitario manage.py para la creación de un nuevo proyecto Django.
  - .gitignore
  - README.md - Documentación
  - .env (variables de entorno)
  - requirements.txt
  - Subir el proyecto a gitHub (privado)

Resumen de Adicional
  - Crear app web
  - Crear una route + view
  - Modular la route a urls.py del project onyFlans



# Requerimientos
1. Crea un entorno virtual llamado onlyflans y una vez activado, comprueba que la versión de python usada es python 3. Realiza un “pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un archivo jpg o png dentro de la carpeta requerimiento1.

2. Instalar django 3.2.4 dentro del entorno virtual onlyflans, una vez instalado verifica que 
haya sido instalado exitosamente utilizando el comando pip freeze. Realiza un 
“pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un 
archivo jpg o png dentro de la carpeta requerimiento2.

3. Usando django-admin genera un proyecto llamado onlyflans, una vez creado ingresa 
a la carpeta del proyecto generado, aplica las migraciones y ejecuta tu servidor 
utilizando los comandos correspondientes del archivo manage.py y accede a la url 
disponible para tu proyecto. Una vez que puedas acceder a la web en tu navegador, 
realiza un “pantallazo” de ésta y guardalo en un archivo jpg o png dentro de la carpeta
requerimiento3.


---

```

```

## DJANGO 3.2.4
### De querer utilizar esa versión, hoy teniendo python 3 podemos tener el error:
Falta el módulo `distutils`, el cual es necesario para que Django funcione correctamente. Este módulo solía ser parte del paquete estándar de Python, pero en las versiones más recientes, puede no estar incluido por defecto.

Solucionar este problema instalando `distutils` manualmente:

1. Tener el entorno virtual activado.
2. Instalar `distutils` usando `pip` o `ensurepip`.

### Opción 1: Usar `ensurepip`
```bash
python -m ensurepip --upgrade
```

### Opción 2: Usar `pip`
Si `ensurepip` no funciona, intentar instalar `distutils` directamente usando `pip`:
```bash
pip install setuptools
```

Luego intentar nuevamente verificar la versión de Django con:
```bash
django-admin --version
```


---


```
```
