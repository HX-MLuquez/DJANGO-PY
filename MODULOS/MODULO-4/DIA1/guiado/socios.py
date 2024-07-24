
#* POO
# Todo es un OBJECT

#* Hacer una class ->
#* definir la class Socio:
#* definir sus atributos (características o cualidades) tienen sus nombres y/o valor
#    - Atributos de clase o estáticos    - Atributos de instancia __init__   requieren del self -> nombre, edad
#* definir los métodos (funciones) 
# - funciones (acciones) dentro de la clase para que interactuen con los atributos de la clase

#* Crear la INSTANCIA  ->   pepe = Socio("Manolo", 3)
#* pepe ES EL OBJECT  pepe.eliminar()   pepe.agregar()  pepe.actualizar()
"""
pepe es un OBJECT - Alegoría con un DICT 
pepe = {
    "nombre": "Manolo",            Atributos - Estado
    "edad": 3,
    -------------------------
    "eliminar": eliminar,
    "agregar": agregar,            Métodos
    "actualizar": actualizar
}
pepe.eliminar() <- Los OBJETOS se pueden acceder a sus propiedades con el dot notation 
print(pepe.nombre) -> Manolo
"""

class Socio:
    temporada = "Verano"
    numero_de_cuotas = 2

    @staticmethod
    def cambiar_temporada(nueva_temporada):
        Socio.temporada = nueva_temporada
        return f'La nueva temporada es {Socio.temporada}'

    @staticmethod
    def incrementa_cuota():
        Socio.numero_de_cuotas += 1
        return f'El número de cuotas es {Socio.numero_de_cuotas}'

    def __init__(self, nombre, apellido, email) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.activo = True
        self.cuotas = ["enero", "febrero"]

    def mostrar_socio(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "activo": self.activo,
            "cuotas": self.cuotas,
        }

    def socio_habilitado(self):
        if len(self.cuotas) < Socio.numero_de_cuotas:
            self.activo = False
        else:
            self.activo = True
            
        if self.activo:
            return "Socio habilitado"
        else:
            return "Socio NO habilitado"
    
    def pagar_cuota(self,cuota):
        self.cuotas.append(cuota)
        return "Cuota pagada"
        
socio_toto = Socio("Toto", "Lopez", "toto@gmail.com")
print(socio_toto.mostrar_socio())

# {'nombre': 'Toto', 'apellido': 'Lopez', 'email': 'toto@gmail.com', 
# 'activo': True, 'cuotas': ['enero', 'febrero']}
print(socio_toto.socio_habilitado()) # Socio habilitado

socio_toto.incrementa_cuota()

print(socio_toto.socio_habilitado())

socio_toto.pagar_cuota("marzo")
print(socio_toto.mostrar_socio())
print(socio_toto.socio_habilitado())

"""
{'nombre': 'Toto', 'apellido': 'Lopez', 'email': 'toto@gmail.com', 'activo': True, 'cuotas': ['enero', 'febrero']}
Socio habilitado
Socio NO habilitado
{'nombre': 'Toto', 'apellido': 'Lopez', 'email': 'toto@gmail.com', 'activo': False, 'cuotas': ['enero', 'febrero', 'marzo']}
Socio habilitado
"""