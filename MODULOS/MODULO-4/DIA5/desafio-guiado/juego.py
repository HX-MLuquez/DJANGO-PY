# Las opciones de juego del usuario, así como el
#  nombre de su personaje, se deben solicitar mediante input.

#  ● Cada personaje tiene un nombre, el cual debe ser especificado al momento de crear
#  un personaje.
#  ● Cada personaje recién creado tiene nivel 1 y experiencia 0 (estos son los únicos
#  valores posibles al momento de crear un personaje).
#  ● Acadapersonaje es posible consultarle o asignarle un estado. Al solicitar el estado
#  de un personaje, se debe mostrar en pantalla su nombre, su nivel y su experiencia. Al
#  asignar un valor al estado, este valor corresponderá a la experiencia recibida por el
#  personaje. 

"""
nombre: mago  nivel: 1 experiencia: 0           |       nombre: Orco  nivel: 1 experiencia: 0 
                                    Posibilidades de ganar 50%
Gana 50  Pierde -30               - random (0,1)  ->    1

nombre: mago  nivel: 1 experiencia: 50           |       nombre: Orco  nivel: 1 experiencia: 0
                                      Posibilidades de ganar 66%
Gana 50  Pierde -30               - random (0,1)  ->    1
nombre: mago  nivel: 1 experiencia: 100   ->  nombre: mago  nivel: 2 experiencia: 0
                                              nombre: Orco  nivel: 1 experiencia: 0
                                            
Gana 50  Pierde -30               - random (0,1)  ->    0
nombre: mago  nivel: 2 experiencia: -30   ->   nombre: mago  nivel: 1 experiencia: 70  

Gana 50  Pierde -30               - random (0,1)  ->    0
nombre: mago  nivel: 1 experiencia: 70   ->    nombre: mago  nivel: 1 experiencia: 40   

Gana 50  Pierde -30               - random (0,1)  ->    0
nombre: mago  nivel: 1 experiencia: 40   ->    nombre: mago  nivel: 1 experiencia: 10   
                                   Posibilidades de ganar 33%
Gana 50  Pierde -30               - random (0,1)  ->    0
nombre: mago  nivel: 1 experiencia: 10     ->  nombre: mago  nivel: 1 experiencia: -20  -> 0                    
"""


# INICIA El jugador debe ingresar 1 para “Atacar” y 2 para “Huir”
# WHILE

# Puede usar uniform() del módulo random.
# random.uniform(0,1)



#  a. Importar módulos necesarios para el desarrollo del juego.
#  b. Creación de personajes y almacenamiento de opción de juego del jugador
#  (calculandoymostrandoprobabilidaddeganar)
#  c. Para la opción de ataque, segúnel resultadoobtenido, actualizaciónde
#  estadosdelospersonajes.
#  d. A continuación del punto anterior, dentro del ataque, mostrar estados
#  actualizadosdelospersonajes, ynuevaconsultaalusuarioconsiderandola
#  probabilidadactualizadadeganar.

from personajes import Personaje 
import random

print("Bienvenido al Juego")

nombre = input("Ingrese el nombre de su personaje: \n> ")

personaje_humano = Personaje(nombre)

print(personaje_humano.estado)

print("OHOOOOO Llegó el Orco para la pelea")

personaje_orco = Personaje("Orco")
print(personaje_orco.estado)

probabilidad_ganar = personaje_humano.get_probabilidad_de_ganar(personaje_orco) # -> 0.33  0.5  0.66

# Usamos mostrar el diálogo y guardar la opción

opcion = Personaje.mostrar_dialogo(probabilidad_ganar) # 1  or  2

while opcion == 1:
    # -------
    resultado = "G"
    if random.uniform(0,1) <  probabilidad_ganar:
        resultado = "G"
    else:
        resultado = "P"
    if resultado == "G":
        print("Has ganado")
        personaje_humano.estado = 50
        personaje_orco.estado = -30
    elif resultado == "P":
        print("Has perdido")
        personaje_humano.estado = -30
        personaje_orco.estado = 50
        
    print(personaje_humano.estado)
    print(personaje_orco.estado)
    # Acá está el corte
    probabilidad_ganar = personaje_humano.get_probabilidad_de_ganar(personaje_orco) # -> 0.33  0.5  0.66
    opcion = Personaje.mostrar_dialogo(probabilidad_ganar)
    
print("Te has retirado")