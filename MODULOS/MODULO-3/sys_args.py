# Librería / Módulo
import sys

# sys.argv

# TODO: Maneras de Ingresar datos

nombre = input("Ingrese su nombre: ")
print(f'Mi nombre es {nombre}')

# * USAMOS SYS.ARGV
print(f'Script -> {sys.argv[0]}')

print(f'primer argumento luego del Script original -> {sys.argv[1]}')
print(f'otro argumento luego del Script original -> {sys.argv[2]}')


print(f'El área del rectángulo es {float(sys.argv[1]) * float(sys.argv[2])}')


#                          0       1    2     3
# Script      sys.argv["day6.py", "3", "4", "pepe"]
# Probar con -> python day6.py 3 4 pepe

#                          0
# Script      sys.argv["day6.py"]
# Probar con -> python day6.py
# sys.argv[1]