def sumar_numeros(num_a, num_b):
    resultado = num_a + num_b
    print("num_a es: ", num_a)
    print("num_b es", num_b)
    global lista_de_todas_las_sumas
    lista_de_todas_las_sumas.append(resultado)
    return resultado

if __name__ == "__main__":
    sumar_numeros(2, 3)