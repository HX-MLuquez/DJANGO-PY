
class Te:
    duracion = 365

    @staticmethod
    def tiempo_y_recomendacion(sabor):
        if sabor == "1":
            return 3, "Al desayuno", "te negro"
        elif sabor == "2":
            return 5, "Al mediodía", "te verde"
        elif sabor == "3":
            return 6, "Al anochecer", "agua de hierbas"

    @staticmethod
    def precio(gramos):
        precio = 0
        if gramos == 300:
            precio = 3000
        elif gramos == 500:
            precio = 5000
        return precio
