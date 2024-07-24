# *args  -> []
# (**kwargs) -> {}  <-  (edad=12, nombre=Mau)

class PelotaDeDeporte():
    def __init__(self, tamaño: int, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de deporte")
        self.tamaño = tamaño


class PelotaDePlastico():
    def __init__(self, material: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de plástico")
        self.material = material


class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de ping pong")
        self.timbre = timbre

    # Salida:
    # Creando pelota de plástico
    # Creando pelota de deporte
    # Creando pelota de ping pong
pdpp = PelotaDePingPong(tamaño=4, material="celuloide", timbre="POWERTI")
