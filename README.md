# Curso Python - Django 2024

## MODULO 6 - CRONOGRAMA

### HITOS

El proyecto estará dividido en 5 hitos incrementales que te permitirán comenzar un proyecto desde las bases, los cuales son:

1. **HITO-1** Levantando tu primer proyecto Django: en este Hito se preparará un ambiente nuevo e inicializará un proyecto Django desde 0.

2. **HITO-2** Creación de un sitio web responsive con Bootstrap: en este Hito se crearán las primeras estructuras que permitirán mostrar datos en nuestro sitio web.

3. **HITO-3** Añadiendo interacción a nuestro sitio web (modelos y formularios): en este Hito se crearán nuevos modelos de datos y se habilitará su interacción a través del panel de administración de Django y de un formulario personalizado.

4. **HITO-4** Manejando perfiles con Django: en este Hito se implementará inicio y cierre de sesión y protegerá una vista para hacerla inaccesible por usuarios no autenticados en el sistema.

5. **HITO-5** Presentación del proyecto: en este Hito se deberá presentar lo desarrollado en los 4 Hitos anteriores, realizando una demostración del código funcional y además explicando distintas particularidades.

---

#### Requerimientos
1. Levantar primer proyecto en Django
  - Utiliza el administrador de paquetes PIP para la instalación de los componentes Django.
  - Utiliza el utilitario manage.py para la creación de un nuevo proyecto Django.

Adicional
  - Crear app web
  - Crear una route + view
  - Modular la route a urls.py del project onyFlans

2. Crear sitio web responsive con Bootstrap
(3 Puntos)
● Implementa un proyecto Django para servir contenido estático dando solución 
a los requerimientos.
● Utiliza templates para la renderización de contenido dinámico en un proyecto 
Django para dar solución a un requerimiento.
● Utiliza herencia de plantillas en un proyecto Django para dar solución a un 
requerimiento.
● Utiliza instrucciones de control en plantillas de un proyecto Django para dar 
solución a un requerimiento.
3. Añadir interacción al sitio web, a través de modelos y formularios
(3 Puntos)
● Utiliza las clases provistas por el framework Django para la integración de un 
formulario básico.
● Procesa un formulario Django utilizando templates para dar solución a un 
requerimiento.
● Implementa plantillas de formulario reutilizables para dar solución a un 
requerimiento.
● Maneja mensajes de errores de formularios en el template para dar solución a 
un requerimiento.
4. Manejar perfiles con Django
(1 Punto)
● Describe las características del modelo de autenticación de Django para el 
control del acceso al aplicativo.
● Describe las características del módulo de permisos y autorización disponible 
en Django para el control del acceso a un recurso.
● Explica el concepto de Mixins en proyectos Django para control y seguridad de 
acceso.
4
● Implementa el modelo Login/Logout de Django para el control del acceso al 
aplicativo.
● Implementa el control de acceso a recursos de vista y de acciones a un 
aplicativo web utilizando el modelo de autorización y permisos de Django.
● Reconoce las características básicas del sitio administrativo de Django y su 
utilidad en el modelo Auth.
● Implementa el módulo administrativo de Django para la administración de 
usuarios.
● Opera el módulo administrativo de Django realizando la administración de 
usuarios y grupos.
5. Presentar proyecto
(2 Puntos)
● Presenta el proyecto modular abordando cada uno de los hitos de creación de 
la aplicación web

---

## GIT + GITHUB - COMANDOS

CLONAR

```bash
git clone https://github.com/HX-MLuquez/DJANGO-PY.git
```

Conectar con REMOTE

```bash
git remote add origin https://github.com/HX-MLuquez/DJANGO-PY.git
```

Para ver si estamos o no actualizados

```bash
git fetch origin master
```

### Comandos GIT + Importantes

**CUIDADO**
Previo ver de estar parado en el path correcto de esta carpeta (proyecto)

```bash
git status
```

**Actualizar**

```bash
git pull origin master
```

```

```

# GIT & GITHUB - COMANDOS para nuestros PROYECTOS

Ver archivos y archivos ocultos

```bash
ls
ls -a
```

## COMANDOS de CONSULTAS

```bash
git status

git log

git remote -m
```

### INICIAR GIT

```bash
git init
```

### PUSHEAR

- git push origin main

### TRAER

- git pull origin main

### VER origin remote

- git remote -> origin

### VER url remote

- git remote -v

```
->
origin  https://github.com/HX-MLuquez/GIT-EXERCISE.git (fetch)
origin  https://github.com/HX-MLuquez/GIT-EXERCISE.git (push)
```

Conectar Repo con Local y pasar master a main

- git remote add origin https://github.com/HX-MLuquez/blabla.git
- git branch -M main

Luego

- git add .
- git commit -m "..."

Para así:

- git push -u origin main

Y luego ya solo

- git add .
- git commit -m "..."
- git push

Ejemplo remote add:

- git remote add [nombre] [dirección del repositorio]

- git remote show [nombre]
  - Ejemplo
  - git remote show https://github.com/HX-MLuquez/GIT-EXERCISE.git

```
->
* remote https://github.com/HX-MLuquez/GIT-EXERCISE.git
  Fetch URL: https://github.com/HX-MLuquez/GIT-EXERCISE.git
  Push  URL: https://github.com/HX-MLuquez/GIT-EXERCISE.git
  HEAD branch: master
  Local ref configured for 'git push':
    master pushes to master (up to date)
```

Renombrar

- git remote rename nombreActual NuevoNombre

ELIMINAR

- git remote rm NombreRepositorio

CLONAR y conectar

- git clone [dirección del repositorio]
- git init
- git remote add origin https://github.com/HX-MLuquez/blabla.git

REVERTIR INIT

Para revertir un git init, que inicializa un nuevo repositorio Git en un directorio, puedes seguir estos pasos:

Eliminar el directorio .git: El comando git init crea un directorio oculto llamado .git en la raíz del repositorio. Eliminar este directorio revertirá el repositorio a su estado antes de ser inicializado. Puedes hacer esto usando el siguiente comando en la terminal:

```bash
rm -rf .git
```

Y reiniciar el repositorio

CRAER Nueva Rama git branch:

```bash
git branch nueva-rama
```

Cambiar de rama:

```bash
git checkout nombre-de-la-rama
```

```



```

---

## Fecha SEMANA PREPARACIÓN-PRUEBA
Curso: 47-1
Code: RLAB-23-02-14-0047-1
Fecha es desde 24/09 al 30/09

---

### Enlace encuesta de cada día

https://forms.gle/m4UkmSVECYhTMQqGA
