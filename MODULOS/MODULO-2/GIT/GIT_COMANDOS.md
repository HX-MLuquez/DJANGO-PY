# GIT & GITHUB

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


# Git branch 

Conociendo las ramas del proyecto
- Una de las principales ventajas de git es la utilización de branch (ramas). Primero 
definiremos una rama simplemente como un camino donde está nuestro código, 
mientras que la definición técnica se refiere a un branch como un apuntador a donde 
van los commits que realizamos.

- Cada vez que inicializamos git, de forma automática se genera un branch main, que es 
donde se guardarán los nuevos commits.

- Al iniciar git en una carpeta, de forma automática se genera la rama main. Podremos 
conocer las ramas que tiene nuestro proyecto con el comando:

- Nos mostrará en consola todos los branch del proyecto. Como solo tenemos una rama, 
nos aparecerá main.

¿Cuándo generar una nueva rama?

- Para crear una nueva branch utilizaremos el siguiente comando:
```bash
git branch nueva_branch
```
- Una vez creado, no cambiará de forma automática a la nueva rama, sino que nos 
quedaremos en la rama original. Para cambiarnos debemos hacerlo con el comando:

```bash
git checkout nueva_branch
```
- Si queremos crear una branch y situarnos enseguida en ella debemos ejecutar el 
siguiente comando:
```bash
git checkout -b otra_branch
```

## Git stash
- Existe una manera de reservar o “apartar” las modificaciones que estamos haciendo en 
nuestra rama actual para realizar una tarea emergente y asegurarnos que no 
perderemos los cambios que hemos realizado,  para esto podemos optar por ocupar el 
comando: 
```bash
git stash
```
- Todos nuestros cambios han desaparecido, sin embargo, lo que sucedió es que fueron 
diferidos a un área en paralelo de nuestro historial de commits al cual podemos 
acceder con el siguiente comando:

```bash
git stash list
```
- Para volver a unir el directorio actual con los cambios que estábamos trabajando y que 
fueron apartados del commit en el que nos encontrábamos.
```bash
git stash apply
```
- Este comando es muy útil para desarrollar sin temor a perder nuestras modificaciones, 
no obstante se recomienda usarlo en casos puntuales donde necesitemos de forma 
urgente solucionar problemas que fueron detectados mientras estamos trabajando en 
una nueva versión de nuestro proyecto.

## Git Rebase 

En cierto sentido, **git rebase y git merge** son herramientas que se utilizan para combinar cambios de diferentes ramas en Git, pero difieren en cómo lo hacen y en el efecto que tienen en el historial de commits.

- Git Merge:

Con git merge, Git crea un nuevo commit de fusión que incorpora los cambios de una rama en otra.
Este commit de fusión tiene dos padres: uno de la rama en la que estabas cuando ejecutaste el comando merge y otro de la rama que estás fusionando.
El historial de commits resultante mostrará claramente la unión de las dos líneas de desarrollo, con un nodo de fusión representando el punto en el que se combinaron las ramas.

- Git Rebase:

Con git rebase, Git toma los cambios de una rama y los aplica secuencialmente sobre otra rama, como si los cambios hubieran sido realizados directamente sobre la rama objetivo.
En lugar de crear un nuevo commit de fusión, git rebase reescribe la historia de commits de la rama que estás rebaseando, moviendo cada commit individual a la punta de la rama objetivo.
Esto resulta en una línea de desarrollo más lineal y limpia, ya que elimina los commits de fusión adicionales que git merge puede generar.

Entonces, en esencia, ambos git merge y git rebase combinan cambios, pero git rebase lo hace reescribiendo la historia de commits, mientras que git merge crea un nuevo commit de fusión

## Git rebase
- Cuando estamos trabajando en un equipo de desarrollo y varios usuarios manipulan el 
mismo repositorio en paralelo, es normal que se generen muchas ramas y muchos 
commits que dificultan la lectura del historial general, puesto que habrán 
modificaciones agrupadas en una rama A que serán unidas a una rama B a partir del 
último cambio generado. 

- Para lograr un historial más limpio con menos ramas y menos commits distribuidos, git 
nos ofrece el siguiente comando:

```bash
git rebase otra_branch
```

Ejemplo:
```bash
(mauro)
cambiar el code

git add .
git commit -m "fufu"

git checkout main

(main)
git rebase mauro
```



```
```

# GitHub PAGES 
Al enderizar nuestro código de una rama específica en un dominio y 
espacio dentro de GitHub.

- Esto será de utilidad para poder mostrar nuestro trabajo de forma gratis, sin tener que 
recurrir a dominios o servidores externos.

## Subiendo una página a GitHub pages
Forma manual a través de la consola:
1. Crearemos la rama:
```bash
 git branch gh-pages
 ```
**Recuerda que el nombre debe ser "gh-pages"**

2. Ahora, pasaremos todos los commits de la rama main a la nueva rama, para luego 
subir los cambios al repositorio remoto.
```bash
 git checkout gh-pages
 git merge main
 git push origin gh-pages
```

3. Finalmente, visitamos la página (reemplaza con tu nombre de usuario y nombre de tu 
repositorio donde corresponde).

4. Podremos ver la página almacenada en GitHub pages, que es completamente online. 
Se la puedes mostrar a quien quieras.

https://TuNombreDeUsuario.GitHub.io/Nombre_de_tu_repositorio

Ejemplo:

https://hx-mluquez.github.io/ricomida-app/

```
A tener en cuenta que a la fecha (mayo 2024) es funcional solamente con código HTML, CSS y JS

El archivo index.html debe estar directo en el raíz (root) y debe estar en minúscula y sin error
de sintáxis 
```


## CONFIGURAR el PAGES desde GITHUB

- Seleccionar Settings (la turquita)
- Seleccionar Pages

