preguntas_basicas = {
    'pregunta_1': {'enunciado':['Enunciado básico 1'],
                     'alternativas': [['alt_1', 0], # 1 2 3 4  -  3-1
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado básico 2'],
                    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
   'pregunta_3': {'enunciado':['Enunciado básico 3'],
                     'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['Enunciado intermedio 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado intermedio 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado intermedio 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['Enunciado avanzado 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado avanzado 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado avanzado 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}



"""
'pregunta_1': {'enunciado':['Enunciado básico 1'],


'alternativas': [['alt_1', 0], ['alt_2', 1], ['alt_3', 0], ['alt_4', 0]]},

                [['alt_3', 0], ['alt_1', 0], ['alt_2', 1], ['alt_4', 0]]},
                
                a                b             c             d
                a = 0            b = 1        
                
                alternativas[0][1] == 0
"""