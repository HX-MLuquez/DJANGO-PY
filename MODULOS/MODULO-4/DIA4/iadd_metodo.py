

class Producto:
    def __init__(self, nombre, stock) -> None:
        self.nombre = nombre
        self.stock = stock

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "stock": self.stock
        }

    # def __eq__(self, otra) -> bool:
    #     return self.nombre == otra.nombre
    
    def __iadd__(self, otra):
        if self.nombre == otra.nombre:
            self.stock += otra.stock
        return self


product1 = Producto("Tv", 3)
product2 = Producto("Tv", 37)
print(product1.to_dict())  # {'nombre': 'Tv', 'stock': 3}

product1 += product2
print(product1.to_dict()) # -> {'nombre': 'Tv', 'stock': 40}
