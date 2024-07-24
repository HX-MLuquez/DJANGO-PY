
import json
from usuario import Usuario
from datetime import datetime
# Usuario
"""
1. Crear un archivo script.py que permita leer línea a línea el archivo usuarios.txt, y crear
una instancia de Usuario a partir de los datos de cada línea leída.

2. En el mismo archivo, manejar las posibles excepciones al leer cada línea y/o generar
cada instancia, y agregar la excepción en un archivo error.log
"""

lista_usuarios = []

indice = 1

try:
    with open("usuarios.txt") as archivo:
        linea = archivo.readline()
        while linea:
            try:
                usuario = json.loads(linea)
                # print(usuario)
                instancia_usuario = Usuario(
                    usuario["nombre"], usuario["apellido"], usuario["email"], usuario["genero"])
                # print(instancia_usuario)
                lista_usuarios.append(instancia_usuario)
                try:
                    print("")
                except:
                    print("")

            except Exception as e:
                with open("error.log", "a+")as log:
                    ahora = datetime.now()
                    log.write(f'{ahora.strftime('%Y-%m-%d %H:%M:%S')}{e}\n')
                    indice += 1
                print(e)
            finally:
                linea = archivo.readline()
except Exception as e:
    print(f"Esperando correcta lectura del archivo .... {e}")

# print(lista_usuarios)
"""
Leer línea por línea usuarios.txt 

Con cada línea intentan crear un usuario (instancia de un usuario)

y si no pueden guardar un error en error.log


try
except
finally

"""
