print("holis, estamos en el día 4 de PYTHON")

# FIN EXPLÍCITO
for i in range(1,5):
    print(i)
print(f'Fin del code')

# FIN IMPLÍCITO
for i in range(1,4):
    print(i)

"""
Tenemos 3 barcos con capacidad de 80 pasajeros y hay en la terminal 1200 personas, debemos ver de como
distribuir a estas personas en los colectivos para realizar la menor cantidad de viajes. Pero todas son
familias de 4 o 5 personas y no quiero dejar separadas a las familias. Cuantos viajes se deben hacer?

¿?? 80 de 5 (400) y el resto de 4 (800)

2 barcos con capacidad 7 personas    3 grupos ->  2 de 5  y 1 de 4
"""


# Iniciamos
#     Entran los datos de la cantidad de personas y barcos
#     Preguntamos si es de grupo de 5 o de 4
#     Si es de 5 los vamos subiendo al barco A
#     Si es

"""

jimy : 15 años, tiene piojos, y no le gustan los deportes
pepe: 18 años, no tiene piojos, y le gustan los deportes
juancito: 12 años, tiene piojos, y le gustan los deportes
timy: 22 años, no tiene piojos, y no le gustan los deportes

        no tiene piojos  XOR  es mayor de edad (>=18) XOR  le gustan los deportes
jimy        False                   False                      False                 NO
pepe        True                    True                       True                  NO  
juancito    False                   False                      True                  SI
timy        True                    True                       False                 SI

        no tiene piojos  OR  es mayor de edad (>=18) OR  le gustan los deportes
jimy        False                   False                      False            NO          
pepe        True                    True                       True             SI               
juancito    False                   False                      True             SI     
timy        True                    True                       False            SI    

        no tiene piojos AND es mayor de edad (>=18) AND le gustan los deportes
jimy        False                   False                      False             NO         
pepe        True                    True                       True              SI             
juancito    False                   False                      True              NO  
timy        True                    True                       False             NO   

"""