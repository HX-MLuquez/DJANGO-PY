# # Se importan muchas Librerías
# # Código que hace muchas cosas interesantes
# # Menú
# print("Te gusta el sol?")
# print('Opciones: ')
# print('1) De acuerdo')
# print('2) En desacuerdo')
# print('3) No me interesa')
# # Más código que hace muchas cosas interesantes
# # Nuevamente el Menú
# print("Te gusta la luna?")
# print('Opciones: ')
# print('1) De acuerdo')
# print('2) En desacuerdo')
# print('3) No me interesa')
# # Otro código que hace muchas cosas interesantes
# # Menú por última vez
# print("Te gusta la guata?")
# print('Opciones: ')
# print('1) De acuerdo')
# print('2) En desacuerdo')
# print('3) No me interesa')
# # Código final y fin del Programa


def imprimir_menu(pregunta):
    print(f'{pregunta}')
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')
    # -> SALIDA
   

imprimir_menu("Te gusta el brócoli?")
imprimir_menu("Te gusta la playa?")
imprimir_menu("Te gusta el frío?") # <- ENTRADA


resultado = imprimir_menu("Te gusta el frío?") #! RETURN -> 

print(resultado) # 