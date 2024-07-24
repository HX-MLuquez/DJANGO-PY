import math  # Librería Nativa de Python
# print("hola")
"""
Ve =√2gr
Ve : corresponde a la Velocidad de Escape en [m/s]. 
g: corresponde a la constante gravitacional en [m/s2]. 
r: Corresponde al radio del planeta en [m].
"""

"""
IN:  
“Ingrese el radio en Kilómetros:”,  
“Ingrese la constante g: ” 
La respuesta del programa también debe mostrarse con un texto apropiado: 
OUTPUT: 
“La velocidad de Escape es 11174.6 [m/s]” 
"""

# * ENTRA UN STRING SIEMPRE <- input() <- siempre nos trae un ""  ---   23 -> "23" -> 23.0
r = float(input('Ingrese el radio en Kilómetros: ')) * 1000
g = float(input('Ingrese la constante g: '))

v_e = math.sqrt(2 * r * g) # 234.686786875678500233

print(f'La velocidad de Escape es {v_e:.1f} [m/s]')  # 11174.6 [m/s]

# round(ve, 1)
print(f'Vamos a ver el code de MATH {math}') # <module 'math' (built-in)>

"""
math {
    ceil: def()
    ...
    ...
    ...
}

"""
