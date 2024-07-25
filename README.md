
# Curso Python - Django 2024

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
- git remote  -> origin

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
- git remote rename nombreActual  NuevoNombre


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