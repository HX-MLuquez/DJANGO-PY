# Instalación Postgres SQL 

1. Ir a https://www.postgresql.org/download/
2. Seleccionar su sistema operativo, en mi caso windows
3. Tocar donde dice Download the installer 
4. Seleccionar la versión, por ejemplo: 10.21 de Windows x86-64 o superior (como la última versión)
5. Descargar 
6. Iniciar instalación 
7. Dar a siguiente siguiente siguiente dejar los 4 programas que nos brinda  
    - PostgreSql Server 
    - Pgadmin
    - Stack Bulder 
    - Command Line Tools 

dar -> Siguiente 

8. IMPORTANTE escribir y recordar (agendar en algún lugar de ser necesario) la contraseña 
9. Siguiente dejar puerto por default y siguiente
10. Configuración regional tb dejar por defecto y siguiente siguiente siguiente
11. Al finalizar instalación NO DESMARCAR stack Bulder y tocar Terminar
12. En la barra de select seleccionar postgresSql... y siguiente
13. IMPORTANTE en el select de categories seleccionar DataBase Drivers y allí dentro 
dejar marcadas todas (las 4) opciones y luego next next y aceptar y dar a siguiente 
para todas las ventanas (4) que se irán instalando. 
14. Listo, dar Finish

Ahora podemos usar postgresSql desde la consola o desde la interfaz gráfica Pgadmin 

PD: si ya lo tienes instalado y no funciona primero lo debes desinstalar toooodooo 
y luego realiza estos 14 pasos.


Listo!!!
Enjoy!!!!!!!!

--------------------------------------------------------------------------------------------------------------

```
```


### EXTRA
# Habilitar comandos de psql en CMD (windows)

Luego de la instalación

1. Copiar la ruta donde están los 3 archivos dentro de la carpeta
 
Ejemplo: 
```bash
C:\Program Files\PostgreSQL\14\bin
```
2. Ir a Este Equipo (botón derecho) 
    - --> abrir propiedades(o en configuración  
    - --> acerca de 
    - -->)
    - luego abrir configuración avanzada del sistema
3. Ir a variables de entorno 
    - -->
    - luego a -> Path 
    - y allí crear nueva dirección con la copiada --> 

Ejemplo: 
```bash
C:\Program Files\PostgreSQL\14\bin
```
Eso habilita ejecutar psql desde cualquier carpeta de nuestra pc

Listo ya podemos usar psql en powershell o en CMD
Enjoy!!!!!!!!

--------------------------------------------------------------------------------------------------------------

### Para ingresar desde otra consola usar el comando:
```bash
psql -U postgres
```
