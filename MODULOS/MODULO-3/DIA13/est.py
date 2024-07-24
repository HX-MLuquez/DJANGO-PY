
import math
lista_test = [3, 4, 3, 3]


def media(lista):
    return sum(lista)/len(lista)
#            13   /   4  =  3.5


def sdd(lista, resultado_media):
    diff = [(elemento-resultado_media)**2 for elemento in lista]
    return math.sqrt(sum(diff)/(len(lista)-1))


def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = [(valor-m)/sd for valor in lista]
    return m, sd, lista_estandarizada


m, des, l_e = resultado(lista_test)

print(m, des, l_e)
# 3.25 0.5 [-0.5, 1.5, -0.5, -0.5]