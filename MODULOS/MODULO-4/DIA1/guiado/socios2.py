

#Todo: Vamos a hacer una clase <-> MOLDE atributos y métodos

class Socios:
    #* ATRIBUTOS
    temporada= "Verano" # Variable - Atributo Estático
    def __init__(self) -> None:
        self.lista_socios = []
    #* MÉTODOS
    def view_list(self):
        return self.lista_socios
    
    def add_socio(self, nombre, edad):
        socio = {
            "nombre": nombre,
            "edad": edad
        }
        self.lista_socios.append(socio)
        return socio

#Todo: Crear el OBJETO por medio de la INSTANCIA
socios_club_a = Socios()

print(socios_club_a) # <__main__.Socios object at 0x000001448BB969F0>
socios_club_a.add_socio("Juan", 32)
# socios_club_a.lista_socios = 32 # DOT NOTATION para acceder y modificar un atributo de manera directa

print(socios_club_a.lista_socios) # -> [{'nombre': 'Juan', 'edad': 32}]

print(socios_club_a.view_list())
socios_club_a.add_socio("Juan", 32)

# socios_club_a.nanana = 101 
# socios_club_a.sisisisis = [[[[]]]]

# print(socios_club_a.sisisisis)


"""
socios_club_a es un OBJECT - Alegoría con un DICT 

global
temporada= "Verano"
socios_club_a = {
    "lista_socios": [ ],            Atributos - Estado
    -------------------------
    "view_list": view_list,
    "add_socio": add_socio,            Métodos
}

socios_club_a.view_list()  -> [ ]
socios_club_a.add_socio("Juan", 32)  ->  {"nombre": "Juan","edad": 32}
"""