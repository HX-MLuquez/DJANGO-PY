import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas -> [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
    ###############################################################
    print(f'{enunciado[0]}\n')
    letras = ["A", "B", "C", "D"]
    for l, o in zip(letras, alternativas):
        print(f'{l}. {o[0]}')
    #* print enunciado
    
    #* armar lista de opciones ["A", "B", "C", "D"]
    #* usar zip  de las opciones con las alternativas
    #* aplicar for para armar lo que se print en cada vuelta
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4