
#TODO: TUPLAS
tupla_ej = ("Abril", 2021, "boby", "frío")
print(type(tupla_ej)) # <class 'tuple'>

coordenadas = (10, 30, 20)
# Desempaquetando
x, y, z = coordenadas

print(x) # 10 

mes, año, perro, clima = tupla_ej
print(clima)

# INDEX
print(tupla_ej[1])


#TODO: FOR para LIST TUPLE SET es igual

for element in tupla_ej:
    print(element)