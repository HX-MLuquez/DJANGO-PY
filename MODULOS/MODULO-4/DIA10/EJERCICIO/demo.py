

from error import HoraError, LargoTextoError
from reunion import Reunion
import re

titulo = None
hora = None
# * REG-EXP
time_re = "^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"

# todo_ SI entra el TRY entra el ELSE
# todo_ pero SI entra el EXCEPT NO entra el ELSE
while True:
    try:
        if titulo is None or len(titulo) > 150:
            titulo = input(
                "\nIngrese título de la reunión (Máximo 150 caracteres):\n")
            if len(titulo) > 150:
                raise LargoTextoError(
                    "Título de la reunión excede máximo de caracteres", titulo, 150)
        if hora is None or re.search(time_re, hora) is None:
            hora = input("\nIngrese hora de la reunión (Formato: HH:MM:SS):\n")
            if re.search(time_re, hora) is None:
                raise HoraError("Formato de Hora debe ser HH:MM:SS.")

    except Exception as e:
        print(f"\n{e}\n")
        continue
    else:
        break
    
r = Reunion(titulo, hora)
print("\nReunión creada correctamente.")