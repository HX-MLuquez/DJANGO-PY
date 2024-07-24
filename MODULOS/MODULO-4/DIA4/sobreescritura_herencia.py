

#* CLASE PADRE 
class Auto:
    def hacer_ruido(self):
        return "RUN run run runnnnn"
    

auto1 = Auto()
print(auto1.hacer_ruido())

#* SUB-CLASE o CLASE HIJA
class Camion(Auto):
    def tocar_bocina(self):
        return "cua cuaaaaaa"
    def hacer_ruido(self): # Sobre-escritura <- pisa
        return "booooooommmmmm"

camion1 = Camion()
print(camion1.tocar_bocina())
print(camion1.hacer_ruido())


#-------------------------------------------------------------------------------------------

#* CLASE PADRE
class Empleado:
    def mostrar_cargo(self):
        return "Empleado de planta"
    def salario(self):
        return "132.000,00"

#* HEREDA todos los Atributos y Métodos de la class Empleado
class Gerente(Empleado):
    def mostrar_cargo(self):
        return "Director General"
    def salario_final(self):
        return "977.000,00"
    
empleado1 = Empleado()
print(empleado1.mostrar_cargo())
print(empleado1.salario())

gerente1 = Gerente()
print(gerente1.mostrar_cargo()) 
print(gerente1.salario()) # Este método es un método heredado de la clase padre Empleado
print(gerente1.salario_final())


"""
*Salida ->
RUN run run runnnnn
cua cuaaaaaa
booooooommmmmm
Empleado de planta
132.000,00
Director General
132.000,00
977.000,00
"""