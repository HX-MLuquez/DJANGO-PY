
# OBJETO con atributos
auto = {
    "modelo": "",
    "marca": "",
    "año": "",
    "km": "",
    "color": ""
}

# Funciones - Métodos

ford_f100 = auto.copy()


ford_f100["modelo"] = 2000
print(ford_f100) # {'modelo': '', 'marca': '', 'a�o': '', 'km': '', 'color': ''}
fiat_uno = auto.copy()
print(fiat_uno)

print("---------------------------------------------------")

#* TODO es un OBJETO
#todo: CLASES
#* CARACTERISTICAS - ATRIBUTOS
#* ACCIONES - MÉTODOS (funciones propias para tal objeto)

"""
!Una clase es un molde donde se almacenan datos de un objeto y se hacen determinadas acciones para esos datos
"""

class Empleado: # Empleado {"nombre": "" } <- self.nombre -> ""   == Empleado.nombre   
    # El constructor, que se alojan aquí los parámetros (SELF)
    def __init__(self, nombre, edad) -> None: #* Este Molde va a tener estos atributos inicialmente
        self.nombre = nombre 
        self.edad = edad 
        
    def mostrar_empleado(self):
        return f'Mi nombre es {self.nombre} y tengo {self.edad} años'
    
    def incrementar_edad_en_uno(self):
        self.edad = self.edad + 1
    
    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad}

if __name__ == "__main__":
    print("01", Empleado) # <class '__main__.Empleado'>

    #* INSTANCIA <- Ejecuté la clase sobre una variable
    manolo = Empleado("Manolo", 34)
    print("02", manolo) # <__main__.Empleado object at 0x0000021D46506DB0>
    print("03", manolo.mostrar_empleado())

    #* OTRA INSTANCIA <- Ejecuté la clase sobre una variable
    juancito = Empleado("Juan", 34)
    print("04", juancito) # <__main__.Empleado object at 0x0000021D46506DB0>
    print("05", juancito.mostrar_empleado())

    juancito.incrementar_edad_en_uno()
    print("06", juancito.mostrar_empleado())

    print("03", manolo.mostrar_empleado())
