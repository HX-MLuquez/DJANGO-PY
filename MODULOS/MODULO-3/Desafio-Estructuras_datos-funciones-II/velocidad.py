velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
             14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
             14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
             14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
             10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
             11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def promedio(lista):
    return sum(lista) / len(lista)


def filtrar(lista):
    valor_promedio = promedio(lista)
    resultado = []
    i = 0
    for v in lista:
        if v > valor_promedio: 
            resultado.append(i)
        i += 1 
    return resultado   
    # return [pos for pos, v in enumerate(lista) if v > valor_promedio ]
    