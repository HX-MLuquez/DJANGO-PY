from pizza import Pizza

print(Pizza)

# * a

print(f"Todas las pizzas tienen tamaño {
      Pizza.tamanio}\n y todas las pizzas valen $ {Pizza.precio}")

# * b
print(f"Salsa de tomate {Pizza.validar(
    "salsa de tomate", ["salsa de tomate", "salsa bbq"])}")

# * c
pizza1 = Pizza()
pizza1.solicitar()

# * d
print(f'''Sus ingredientes vegetales son: {pizza1.vegetal1} y {pizza1.vegetal2},\n el\ 
      ingrediente proteico es: {pizza1.proteico}\n y el tipo de masa es: {pizza1.tipo_masa},\n y esta pizza ¿Es una pizza válida? {pizza1.es_valido}''')


# ingredientes vegetales, el ingrediente proteico y el tipo de masa 

#* e

print(Pizza.es_valido)
#! AttributeError: type object 'Pizza' has no attribute 'es_valido'

"""
En un archivo llamado evaluaciones.py, importe la clase creada en el requerimiento 
1 (conteniendo los requerimientos 2, 3 y 4), y realice lo siguiente: 
(3 Puntos) 
a. Usar la función print(), para que al ejecutar el script se muestre en pantalla los 
valores de los atributos de clase de la clase importada, sin crear una instancia 
de ella. 
b. Usar la función print(), para que al ejecutar el script se muestre en pantalla 
si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de 
tomate", "salsa bbq"]. Para ello use el método creado en el requerimiento 
2, sin crear una instancia de la clase importada. 
c. Crear una instancia de la clase importada, y luego llamar al método del 
requerimiento 3, para que al ejecutar el script se solicite ingredientes y tipo de 
masa al usuario. 
d. Usar la función print(), para que al ejecutar el script, luego de que el usuario 
haya ingresado los ingredientes y tipo de masa, se muestre en pantalla los 
ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia 
creada en el paso anterior, y si esa instancia es una pizza válida o no. 
e. Usar la función print(), para mostrar en pantalla si la clase Pizza es una pizza 
válida o no, haciendo uso del atributo creado en el requerimiento 4, sin crear 
una instancia de la clase. En este punto, la ejecución del script debe mostrar 
un error (todos los pasos anteriores se deben haber ejecutado correctamente). 
"""