
def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

preguntas = ['Enunciado Pregunta 1','Enunciado Pregunta 2','Enunciado Pregunta 3', 'Te gusta el frío?']
respuestas = []


def genera_preguntas():
    for pregunta in preguntas:
        print(pregunta)
        imprimir_menu()
        respuesta = input("> ")
        respuestas.append(respuesta)

genera_preguntas()

def mostrar_respuestas():
    i = 1
    for r in respuestas:
        print(f'La respuesta a la {i}° pregunta fue {r}')
        i += 1 

mostrar_respuestas()

print("Gracias, bye bye")
