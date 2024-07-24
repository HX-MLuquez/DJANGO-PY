
class Aaa:
    def saludo(self):
        print("aiaiaiaiaiaia")
        
class Bbb(Aaa):
    def saludoNe(self):
        print("bebe")
        
class Ccc(Aaa):
    def saludo(self):
        print("cece")

#* ->     IZQ
class Ddd(Bbb, Ccc):
    def saludoNo(self):
        print("dede")
        
ejemplo = Ddd()
ejemplo.saludo() # dede

# JERARQUÍA
# 1° Dentro de la clase en sí
# 2° La clase Padre, y de tener 2 la de la IZQ
# 3° La que le sigue a la derecha
# 4° Cualquiera que esté por encima