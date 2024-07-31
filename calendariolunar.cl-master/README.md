# calendariolunar.cl
Lunar Phases Calendar written in Python 3 with Django 2

##### Commands
Create spanish translation .po files (verbose mode)
``` bash
python manage.py makemessages -v 3 --locale es
```

Compile .po files into .mo files (not tracked in repo)
``` bash
python manage.py compilemessages
```

# COMO RE-UTILIZO un proyecto como este
1. Los descargan o clonan
2. Abrir en terminal donde se encuantra el manage.py
3. Crean entorno virtual
```bash
virtualenv venv
```
4. Activan el entorno virtual
```bash
source venv/Scripts/activate
```
5. Si hay archivo requirements.txt ejecutan:
```bash
pip install -r requirements.txt
```
6. 
``` bash
python manage.py makemessages -v 3 --locale es
```
7. 
``` bash
python manage.py compilemessages
```
8. Migrate
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
9. Levantar el SERVER
```bash
python manage.py runserver
```