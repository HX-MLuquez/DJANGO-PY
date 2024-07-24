
#                        []    , number
def extremo_multiplicado(lista, factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor*minimo, factor*maximo


# print(extremo_multiplicado(4, [1, 2, 3, 4])) #! ERROR

# Se entregan en orden
print(extremo_multiplicado([1, 2, 3, 4], 4))  # * OK

# Sin orden pero con nombre + valor
print(extremo_multiplicado(factor=4, lista=[1, 2, 3, 4]))  # * OK


def elevar(base, exponente, redondear=False): # VALOR por DEFECTO
    if redondear:
        
        valor = round(base**exponente, 2)
    else:
        valor = base**exponente
    return valor


print(elevar(2.5, 3))
