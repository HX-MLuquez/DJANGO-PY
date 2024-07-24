class Pelota:
    #! Atributo estático -> Pelota.color
    color= "Amarillo"
    def __init__(self) -> None:
        self.color = "Blanco" #! Atributo de INSTANCIA
    # Método de instancia que asigna color
    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color #! Atributo de INSTANCIA
    # Método de instancia que lee color de la instancia
    def lee_color(self):
        print(f"El color de esta pelota es {self.color}") #! Atributo de INSTANCIA
    
    def lee_color_local_y_atributo(self, color_local: str):
        # Esta variable "color" sólo existe en el alcance del método
        color = color_local # Azul
        # Un método de instancia puede llamar a otros métodos
        self.lee_color()
        print(f'eeeeee es self color {self.color}')
        print(f"El color {color} NO es el color de ESTA pelota")

mi_pelota = Pelota()

mi_pelota.lee_color() # Blanco

print(Pelota.color) # Amarillo

mi_pelota.lee_color_local_y_atributo("Azul")
# El color de esta pelota es Blanco
# El color Azul NO es el color de ESTA pelota <- Lee el valor de la variable
