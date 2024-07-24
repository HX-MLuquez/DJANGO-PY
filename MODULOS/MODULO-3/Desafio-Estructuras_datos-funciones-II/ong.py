# calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6) 

def productoria(lista):
    valor = 1
    for element in lista:
        valor *= element
    return valor 


def factorial(num):
    if num < 0:
        print("error")
    if num == 0: 
        return 1 

    resultado = 1
    while num:
        resultado *= num
        num -= 1
    return resultado

#print(factorial(3))

def calcular(**diccionario):
    for k,v in diccionario.items():
        if "fact" in k:  #  k[0] == "f"
            print("")
