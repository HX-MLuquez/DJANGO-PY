

class Pelota:
    def __init__(self, color) -> None:
        self._color = color # color ->  RECURSIVIDAD x Error en sintaxis -> SOLUCIÓN _color
        
    @property 
    def color(self):
        return self._color
    
    @color.setter
    def color (self, nuevo_color):
        print("Dentro del setter color")
        self._color = nuevo_color


pelota1 = Pelota("rojo") # RecursionError: maximum recursion depth exceeded

print(pelota1.color)

pelota1.color = "Amarillo"

print(pelota1.color)
# def pepe():
#     print("holis")
#     return pepe()
# pepe() # RecursionError: maximum recursion depth exceeded


class Cuenta:
    def __init__(self, num_a, num_b) -> None:
        self.num_a = num_a
        self.num_b = self.num_a + num_b # Error