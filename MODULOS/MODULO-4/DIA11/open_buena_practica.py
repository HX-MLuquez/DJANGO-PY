


archivo = open('ejemplo.txt', 'r')
contenido = archivo.read()
print("01", contenido)
print("02", archivo.read())
archivo.close()

print("03", contenido)
# print("04", archivo.read()) #! ValueError: I/O operation on closed file.


with open('ejemplo.txt', 'r') as file:
    contenido2 = file.read()
    print(f'->{contenido2}')

