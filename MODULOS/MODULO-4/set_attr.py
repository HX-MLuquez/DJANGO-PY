
#TODO: __setattr__

class Pelota:
    def __init__(self):   
        self.color = ""  #* Atributo color (de instancia)
    def iniciar_color(self,color): #* Método iniciar_color
        self.color = color
        print(f'el color asignado a self.color es {self.color}')
        # def __setattr__(): #! Se auto ejecuta
        #     super().__setattr__()
        
# Se crea objeto y por medio de INSTANCIA (en línea 11)
pelota_de_andy = Pelota()
pelota_de_andy.iniciar_color("Amarillo") #-> self.color pasa a tener el valor "Amarillo"


#* Se modifica estado (atributos) desde AFUERA usando el DOT NOTATION
pelota_de_andy.color = []

pelota_de_andy.fefe = 21 
pelota_de_andy.juju = "holis"

print(pelota_de_andy.color)

"""
en la línea 11 el 
OBJETO pelota_de_andy = {
    color: "",                  Atributos
    fefe: 21,
    juju: "holis
    ------------------------------
    iniciar_color: def          Métodos
}

"""
