
# * CLASE - MOLDE
class Empleado:
    salario = 400000  # Atributo estático valor igual para todas las instancias (es un atr. de clase)

    def __init__(self, nombre, apellido, edad, antiguedad) -> None: # Atributos de INSTANCIA
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.antiguedad = antiguedad
    def mostrar_empleado(self): # Cada vez que se necesita trabajar con Atributos de INSTANCIA (__init__)
        # Debemos usar el SELF como parámetro
        # return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Antiguedad: {self.antiguedad}' 
        return {
            "nombre": self.nombre,
            "apellido": self.apellido, 
            "edad": self.edad, 
            "antiguedad": self.antiguedad
        }
    
    def editar_antiguedad(self):
        self.antiguedad += 1
        return f'{self.nombre} {self.apellido}, su Antiguedad se actualizó a {self.antiguedad} años'
    
    def salario_real(self):
        porcentaje = self.antiguedad * Empleado.salario / 100 
        resultado =  Empleado.salario + porcentaje
        
        return f'El salario de {self.nombre} {self.apellido} es $ {resultado}'
        
    @staticmethod
    def ver_salario_minimo():
        return Empleado.salario

print(Empleado) # <class '__main__.Empleado'>
print(Empleado.salario) # 400000

# * INSTANCIA -> OBTENER OBJETOS de ese MOLDE

empleado1 = Empleado("Manolo", "Lopez", 32, 10)

print(empleado1) # <__main__.Empleado object at 0x00000212C097A9F0>
print(empleado1.nombre) # Manolo

print(empleado1.mostrar_empleado())
print(empleado1.ver_salario_minimo())

print(empleado1.editar_antiguedad())

print(empleado1.salario_real())


# * OTRA INSTANCIA -> OBTENER OTRO OBJETO Empleado de ese MOLDE

empleado2 = Empleado("Jimy", "Perez", 12, 2)
print(empleado2.mostrar_empleado())
print(empleado2.editar_antiguedad())
print(empleado2.editar_antiguedad())
print(empleado2.salario_real())


# print(Empleado.edad) #! Error


#TODO -> 2 minutos para hacer ENCUESTA <- https://forms.gle/m4UkmSVECYhTMQqGA 

