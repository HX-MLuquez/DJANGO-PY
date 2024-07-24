# GITHUB

PUSHEAR
- git push origin main

TRAER
- git pull origin main

VER origin remote
- git remote  -> origin

VER url remote
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


```
# GITHUB

## Comandos básicos

- `git push origin main`: Sube los cambios locales al repositorio remoto en la rama "main".
- `git pull origin main`: Descarga los cambios del repositorio remoto en la rama "main" y los fusiona con tu rama local.
- `git remote`: Muestra los nombres de los repositorios remotos configurados.
- `git remote -v`: Muestra las URL de los repositorios remotos.

## Configuración inicial del repositorio

```bash
git remote add origin https://github.com/HX-MLuquez/blabla.git
git branch -M main
```
Subir cambios al repositorio
```bash
git add .
git commit -m "..."
git push -u origin main
```
Subsecuentes subidas de cambios
```bash
git add .
git commit -m "..."
git push
```
### Gestión de repositorios remotos
- git remote add [nombre] [dirección del repositorio]: Agrega un nuevo repositorio remoto.
- git remote show [nombre]: Muestra información detallada sobre un repositorio remoto.
- git remote rename nombreActual NuevoNombre: Renombra un repositorio remoto.
- git remote rm NombreRepositorio: Elimina un repositorio remoto.

### Clonar un repositorio
```bash
git clone [dirección del repositorio]
```
### Iniciar un repositorio local
```bash
git init
git remote add origin https://github.com/HX-MLuquez/blabla.git
```

**Notas adicionales:**

Recuerda reemplazar "[dirección del repositorio]" con la URL de tu repositorio en GitHub.

- Los comandos:
    - git add . 
    - git commit -m "..." 
    - git push 
    
Son necesarios para agregar cambios, confirmarlos y subirlos al repositorio remoto.

Siempre es recomendable revisar la documentación oficial de Git y GitHub para obtener información detallada sobre cada comando y su uso.


```
```


# GIT

```bash
git --version
```

## CONFIGURAR LOCAL con GITHUB
```bash
git config --global user.name "TuNombre"
git config --global user.email tucorreo@mail.com

git config --list
```

## INICIAR GIT
```bash
git init
```

## CONSULTAR
```bash
git status
```

## GUARDAR una versión (save)
```bash
git add .

git commit -m "..."
```

## CONSULTAR
```bash
git status
```

```bash
git diff
```
- Para salir de diff presionamos -> Q

## VER diferentes COMMITS

```bash
git log
```

## MOVERNOS a otro COMMIT
```bash
git cherry-pick elNombreCodeDelCommitAlQueQueremosIr
```

- git cherry-pick --continue  || aplicar el Resolve aceptando el INCOMING y MERGE + COMMIT

```bash
git cherry-pick --quit
```
- || git checkout master


## Crear nueva rama

```bash
git branch nombreRama

git checkout nombreRama
```




(git checkout elNombreCodeDelCommitAlQueQueremosIr)
