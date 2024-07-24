from sumar import sumar_numeros
from multiplicar import multiplicar
# ((a + b) * c) - d
lista_de_todas_las_sumas = [2, 3, 4, 32]


if __name__ == "__main__":
    primero_sumo = sumar_numeros(3, -2.21)  # 7
    # print(primero_sumo)
    print(lista_de_todas_las_sumas)  # [2, 3, 4, 32, 7]

    resultado_multiplicar = multiplicar(21, primero_sumo)
    print(resultado_multiplicar)
