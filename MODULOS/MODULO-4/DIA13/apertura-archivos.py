"""
Continuando con el ejercicio guiado "Generación de objetos a partir de un archivo" del archivo 
"Presentación - Manejo de archivos con Python", le solicitan envuelva todo lo que está dentro 
del ciclo while dentro de un bloque try/except. 
● Dentro de la cláusula except, escriba el contenido de la excepción (como str) en un 
archivo error.log. 
● El contenido debe ser añadido al final del archivo error.log, sin borrar su contenido 
previo. 
● La siguiente línea del documento de productos debe leerse al final del bloque 
try/except
"""

import json
from datetime import datetime


class Producto:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio
        
lista_productos = []

try: 
    with open("productas.txt", "r") as productos:
        linea = productos.readline()
        while linea: 
            try:
                producto = json.loads(linea) 
                producto_instancia = Producto(producto.get("nombre"), producto.get("precio"))
                lista_productos.append(producto_instancia)
                print("Producto agregado")
            except Exception as e:
                print(f"{e}")
                with open("error.log", "a+")as log:
                    fecha = datetime.now()
                    log.write(f'{fecha.strftime('%Y-%m-%d %H:%M:%S')} ERROR {e}\n')
            finally:
                linea = productos.readline()
                print(linea)
except Exception as e:
    print(f"No se puede acceder al archivo.... {e}")
    
               
