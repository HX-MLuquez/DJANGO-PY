

class Animal:
    def __init__(self) -> None:
        self.nana = "nana"
        
        
class Perro(Animal):
    def canta(self):
        print("jujujuj")
        
class Gato(Animal):
    def canta(self):
        print("jijiji")

perro1 = Perro()
gato2 = Gato()
print(isinstance(perro1, Perro))
print(isinstance(perro1, Animal))
print(isinstance(gato2, Perro))
print(isinstance(gato2, Gato))