

# SOBRECARGA - SOBRE-ESCRITURA


class OperacionesMatematicas:
    def sumar(self, a, b):
        return a + b

    def sumar(self, a, b, c):
        return a + b + c


operar1 = OperacionesMatematicas()
print(operar1.sumar(2, 5, 6))
