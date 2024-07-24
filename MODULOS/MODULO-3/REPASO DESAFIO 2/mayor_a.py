# python mayor_a.py 40000
# {'Mayo': 81000, 'Agosto': 41200, 'Noviembre': 91000}

import sys

valor = int(sys.argv[1])
print(valor)

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

result = {k: v for k, v in ventas.items() if v > valor}

print(result)
