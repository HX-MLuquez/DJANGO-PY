

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

    def __str__(self) -> str:
        return f'nombre: {self.nombre}, stock: {self.stock}, descuento: {self.descuento_aplicado}, total: {self.precio_final}'


nombre = "Ibuprofeno"
stock = 21
precio_bruto = 11000

med1 = Medicamento(nombre, stock)

med1.precio_final = 11000

print(med1.precio_final)

print(med1)

# -> nombre: Ibuprofeno, stock: 21, descuento: 0.1, total: 11682.0


# -> precio_bruto
# precio_final = precio_bruto + (precio_bruto * iva)
# precio_final = precio_final - (descuento1 * precio_final)
"""
El precio bruto se debe asignar en una instancia ya creada. Al ser 
asignado, en caso de que sea mayor a 0, se debe asignar a la vez el precio 
bruto del medicamento, el descuento y el precio final. El descuento se debe 
aplicar sobre el precio bruto más el IVA, y solo se aplicará en caso de que el 
valor del medicamento esté entre $10.000 y $19.999 (10% de descuento), o 
sea mayor o igual a $20.000 (20% de descuento). 

Finalmente, el script debe mostrar en pantalla el nombre del medicamento 
ingresado y su precio bruto. En caso de tener descuento, también lo debe mostrar 
en pantalla. Por último, debe mostrar también por pantalla el precio final 
(considerando IVA y descuento).
"""
