
# chunk_size = 7

with open("mi_archivo.txt", "r") as archivo:
    bloque = archivo.read(8)
    while bloque:
        print(bloque)
        bloque = archivo.read(8)
