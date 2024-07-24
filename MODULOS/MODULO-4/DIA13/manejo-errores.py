"""
Continuando con el ejercicio guiado "Validación de datos" del archivo "Presentación - Manejo 
de Errores y Excepciones", le solicitan esta vez agregar el atributo “fecha” a las reuniones. Se 
debe validar que la fecha tenga el formato “DD/MM/AAAA”.
Tip: Puede usar la siguiente expresión regular:
^([0-3]?\d\/{1})([01]?\d\/{1})([12]{1}\d{3}?)$
"""

import re

date_re = "^([0-3]?\d\/{1})([01]?\d\/{1})([12]{1}\d{3}?)$"

class FechaError(Exception):
    pass 


class Reunion:
    def __init__(self, titulo: str, hora: str, fecha: str) -> None:
        self.titulo = titulo
        self.hora = hora
        self.fecha = fecha

fecha = None
titulo = "Demo reunión"
hora = "12:00"
reu = None
try:
    if fecha is None:
        fecha = input("Ingrese fecha (formato “DD/MM/AAAA”): ")
    if re.search(date_re, fecha) is None:
        raise FechaError("Formato incorrecto")
    reu = Reunion(titulo, hora, fecha)
    print("Reunion creada")
except FechaError as f:
    print(f"Error: {f}")
finally:
    if reu is None:
        reu = Reunion(titulo, hora, "12/02/1234")
        print("Creamos reunión por defecto con fecha ....")
    else:
        print("FIN")
    
        
    




# resultado = re.search(date_re, "12/03/1234")
# print(resultado)  # <re.Match object; span=(0, 10), match='12/03/1234'>


# resultado2 = re.search(date_re, "sdfgsdfgs")
# print(resultado2)  # None

# if resultado2 is not None:   # None == None  True   ->  None != None False
#     print("genial")
# else:
#     print("acá si")
    


