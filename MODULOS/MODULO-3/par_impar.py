
# TODO: Determinar si el número que nuestro usuario ingresa es par o impar

value = int(input("Ingrese un número > "))  # STRING -> INT
result = value % 2
# print(f"--> {value % 2}")
print(type(value))

if value == 0:
    print("Debe ser diferente a cero")
elif result != 0:
    print("Este número es impar")
else:
    print("Este número es PAR")
