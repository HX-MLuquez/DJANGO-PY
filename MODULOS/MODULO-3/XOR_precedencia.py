print(6 >= 6 or 4 > 5)

print(6 >= 6 ^ 6 > 15)
print((6 >= 6) ^ (4 > 5))

print("------------Identificación de operadores y precedencia------------")
"""
Identificación de operadores y precedencia:

En esta expresión, hay tres operadores: >=, ^, y >.
La precedencia de los operadores en Python es la siguiente:
^ (bitwise XOR) tiene una mayor precedencia que >= (mayor o igual que) y > (mayor que).

Evaluación de las comparaciones:

Python evaluará los operadores según su precedencia.
Primero se debe evaluar la parte 6 ^ 4.
Aplicación del operador XOR (^):

6 ^ 4 se evalúa como una operación bitwise XOR.
En binario:
6 es 110
4 es 100
La operación XOR bit a bit es:

110
100   XOR
----
010
El resultado de 6 ^ 4 es 2 (en decimal).
Sustitución del resultado en la expresión original:

La expresión ahora se simplifica a 6 >= 2 > 5.
Evaluación de las comparaciones (de izquierda a derecha):

Primero se evalúa 6 >= 2, que es True.
Luego se evalúa True > 5, pero en Python True se trata como 1 y False como 0.
Así, la comparación real es 1 > 5, que es False.
Resultado final
"""
print("xor de 6 y 4 -> ", 6 ^ 4)
print("xor de 10 y 3 -> ", 10 ^ 3) # -> 9
"""
El operador XOR (o "exclusive or") realiza una operación a nivel de bits en los números 
que se le proporcionan. La operación XOR devuelve 1 en cada posición de bit donde los bits 
correspondientes de los operandos son diferentes y 0 donde son iguales. 
1010   (10 en binario)
0011   (3 en binario)
----
1001   (resultado de la operación XOR) que corresponde a -> 9
"""
print(6 >= 6 ^ 4 > 5)  # Devuelve False
# Ya que equivale a:
print(6 >= 2 > 5)
# Esto debe dar True
print(6 >= 6 ^ 4 < 3) 
# Y esto dará True ya que la pregunta final es si 1 (del True) es menor a 3
print(6 >= 2 < 3 )
