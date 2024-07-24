class PelotaDeDeporte():
    def __init__(self, tamaño: int):
        print("Creando pelota de deporte")
        self.tamaño = tamaño


class PelotaDePlastico():
    def __init__(self, material: str):
        print("Creando pelota de plástico")
        self.material = material


class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, tamaño: int, material: str, timbre: str):
        # super().__init__(tamaño)
        PelotaDeDeporte.__init__(self, tamaño)
        PelotaDePlastico.__init__(self, material)
        print("Creando pelota de ping pong")
        self.timbre = timbre

    # Salida:
    # Creando pelota de deporte
    # Creando pelota de plástico
    # Creando pelota de ping pong
pdpp = PelotaDePingPong(4, "celuloide", "POWERTI")
