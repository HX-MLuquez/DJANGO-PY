from poo import Empleado  #* <class >

from string import Template

#* INSTANCIA
jose = Empleado("José", 47)
print(jose) # <Object > <poo.Empleado object at 0x00000167307C6570>

print(jose.mostrar_empleado()) # Mi nombre es José y tengo 47 años

print(jose.incrementar_edad_en_uno()) # None

print(jose.mostrar_empleado())

print(jose.to_dict()) # {'nombre': 'José', 'edad': 48}


#TODO: ORDEN de crear OBJETOS por medio de CLASS
#* 1. Crear una CLASS
#* 2. INSTANCIAR la CLASS en una variable
#* 3. ENJOY!!! la variable ya es un OBJETO que ha heredado todos los atributos y métodos de la clase instanciada

#* 2. INSTANCIAR la CLASS en una variable
#* 3. ENJOY!!! la variable ya es un OBJETO que ha heredado todos los atributos y métodos de la clase instanciada

#* 2. INSTANCIAR la CLASS en una variable
#* 3. ENJOY!!! la variable ya es un OBJETO que ha heredado todos los atributos y métodos de la clase instanciada

#* 2. INSTANCIAR la CLASS en una variable
#* 3. ENJOY!!! la variable ya es un OBJETO que ha heredado todos los atributos y métodos de la clase instanciada

