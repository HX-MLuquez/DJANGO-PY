

# #* ATRIBUTOS No ESTÁTICOS (Instanciados __init__) & EStÁTICOS


# class Persona:

#     cantidad_personas = 0 # ESTÁTICO

#     def __init__(self, nombre, altura) -> None: # DE INSTANCIA o NO ESTÁTICOS
#         self.nombre = nombre
#         self.altura = altura
#         Persona.cantidad_personas += 1

#     def modificar_altura(self, nueva_altura):
#         self.altura = nueva_altura

#     def mostrar_persona(self):
#         return {"nombre": self.nombre, "altura": self.altura}

#     @staticmethod # DECORADOR == FUNCIONES #! @staticmethod
#     def ver_cantidad_personas():
#         return Persona.cantidad_personas

# # Accedemos a atributo (variable) ESTÁTICA - NO es necesario crear instancia
# print(Persona.cantidad_personas)


# # IMPLEMENTAR un MOLDE - pasar de la CLASE a un OBJETO
# #! INSTANCIA

# hulk = Persona("Hulk", 2)
# print(hulk.mostrar_persona()) # {'nombre': 'Hulk', 'altura': 2}
# print(hulk.ver_cantidad_personas())

# pepe = Persona("Pepe", 1.4) # pepe es una variable - es una INSTANCIA
# print(pepe.ver_cantidad_personas())

# [].append("2")

# # pepe tiene todos atributos y métodos de la class Persona

# print(isinstance(pepe, Persona)) # True

print("-------------------------------------")


class Auto:
    def __init__(self, modelo, marca, color, km) -> None:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.km = km
        self.acelerar = False
        self.partes = ["ruedas", "volante", "puertas"]

    def mostrar_auto(self):
        return {
            "modelo": self.modelo,
            "marca": self.marca,
            "color": self.color,
            "km": self.km,
            "acelerar": self.acelerar,
            "partes": self.partes,
        }

    def agregar_partes(self, parte):
        self.partes.append(parte)
        return "Parte agregada"

# * HACER INSTANCIA - tomar MOLDE class y pasaría a OBJECT


ford_1 = Auto("1988", "F-100", "Azul", 150321)
# * LOS VALORES de los ATRIBUTOS en este momento se llaman STATE
print(ford_1.mostrar_auto())

# {'modelo': '1988', 'marca': 'F-100', 'color': 'Azul', 'km': 150321, 'acelerar': False, 'partes': ['ruedas', 'volante', 'puertas']}
ford_1.agregar_partes("caja cerrada")
# OTRA INSTANCIA - OTRO AUTO
ford_2 = Auto("2025", "F-300", "Invisible", 2)
print(ford_2.mostrar_auto())

print(ford_1.mostrar_auto())


print("----------------------------------")


class Contador:
    #* Las variable (sin self) - Estáticas
    contador_estatico = 0
    #* Constructor - INICIALIZAMOS los ATRIBUTOS - SELF
    def __init__(self) -> None:
        self.cantidad = 0
        
    def incrementar(self):
        self.cantidad += 1
        print(self.cantidad)

    def mostrar(self):
        print(self.cantidad)
    
    @staticmethod
    def incrementar_contador():
        Contador.contador_estatico += 1
        print(Contador.contador_estatico)


contador1 = Contador()

contador2 = Contador()

contador3 = Contador()

contador3.incrementar() # 1
contador3.incrementar() # 2
contador3.incrementar() # 3

contador2.incrementar() # 1

contador1.mostrar() # 0


contador3.incrementar_contador() # 1
contador3.incrementar_contador() # 2
contador3.incrementar_contador() # 3

contador2.incrementar_contador() # 4

contador1.incrementar_contador() # 5


