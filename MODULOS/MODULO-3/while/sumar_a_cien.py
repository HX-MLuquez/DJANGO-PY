"""
Sumando de 1 a 100
 1 + 2 + 3 + ... + 100 = ¿?
 
Resolver esto es muy similar a contar cien veces, pero además de contar, se debe ir 
guardando la suma acumulada en cada iteración.

 Tips: 
    ● Itera 100 veces.
    ● En cada iteración, utiliza un contador para almacenar la iteración.
    ● En cada iteración, asegúrate de utilizar un acumulador para acumular tus contadores.
    ● El acumulador luego de terminado el ciclo, corresponderá al resultado de la suma.
    ● Asegúrate de iniciar el contador y el acumulador antes de entrar al ciclo.
"""
i = 0
acumul = 0
while i < 100: # 0 - 99
    i += 1 # ... ... -> 101 Cierra el Bloque -> línea 17 101 <= 100 False Fin del Ciclo
    acumul += i

print(f'Valor i = {i} acumula = {acumul}')
# -> Valor i = 101 acumula = 5050 (siempre deben haber 100 iteraciones)

# -> Valor i = 100 acumula = 4950 (siempre deben haber 100 iteraciones)

# -> Valor i = 100 acumula = 5050 (siempre deben haber 100 iteraciones)