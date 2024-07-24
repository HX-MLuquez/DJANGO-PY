

class Medicamento:
    iva = 0.18

    def __init__(self, nombre, stock=0) -> None:
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self._precio_final = 0
        self.descuento1 = 0.1
        self.descuento2 = 0.2
        self.descuento_aplicado = 0

    @staticmethod
    def validar_mayor_a_cero(num):
        return num > 0  # -> return BOOLEANO

    @property               # GETTER
    def precio_final(self):
        return self._precio_final

    @precio_final.setter    # SETTER
    def precio_final(self, precio_bruto):
        print("Dentro del SETTER (mutador) que se encargará de modificar _precio_final")
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            precio_intermedio = precio_bruto + precio_bruto * Medicamento.iva
            
            if precio_intermedio >= 10000 and precio_intermedio < 20000:
                self._precio_final = precio_intermedio - precio_intermedio * self.descuento1
                self.descuento_aplicado = self.descuento1
            elif precio_intermedio >= 20000:
                self._precio_final = precio_intermedio - precio_intermedio * self.descuento2
                self.descuento_aplicado = self.descuento2
            else:
                self._precio_final = precio_intermedio

    def __eq__(self, other):
       return self.nombre.lower() == other.nombre.lower()
   
    def __iadd__(self, other):
       if self == other:
           self.stock += other.stock
       return self


    def __str__(self) -> str:
        return f'nombre: {self.nombre}, stock: {self.stock}, descuento: {self.descuento_aplicado}, total: {self.precio_final}'



med1 = Medicamento("Ibuprofeno", 21)

med1.precio_final = 11000

print(med1.precio_final)

print(med1) # nombre: Ibuprofeno, stock: 21, descuento: 0.1, total: 11682.0

"""
11682.0
nombre: Ibuprofeno, stock: 21, descuento: 0.1, total: 11682.0
"""

med2 = Medicamento("Ibuprofeno", 10)
med2.precio_final = 9000

med1 += med2 
print(med1) # nombre: Ibuprofeno, stock: 31, descuento: 0.1, total: 11682.0

