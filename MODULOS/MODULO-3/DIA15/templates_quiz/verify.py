import preguntas as p

# alternativas -> [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]],  "b"
def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    print(eleccion) # -> index 1
    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    if alternativas[eleccion][1] == 1:
        print("Respuesta correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False
    #* Para determinar la CORRECTA de la NO correcta
    #* Ver en la lIST alternativas que hay 2 elementos
    #* y el de la pos 1 determina 1 para Correcto y 0 para No correcto
    
    return # BOOLEAN
    
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






