
# EL SCOPE (ALCANCE va desde ADENTRO hacia AFUERA)

# GLOBAL
continente = "Africa"

def suma(): #* LOCAL (NIVEL 1)
    # print(1, continente) # 
    # global continente #! Enlasa y Pisa
    continente = "Américaaa"
    print(2, continente)
    def otra(): #* LOCAL (NIVEL 2)
        # continente = "Europa" # Local -> IN function otra
        print(4, continente)
    otra()
    return continente

suma()
print(3, continente)

resultado = suma()


nombre = "Mau"
nombre = 101


lista = ["we", "fe", "se"]

texto = ", ".join(lista)

print(texto) # "we, fe, se"