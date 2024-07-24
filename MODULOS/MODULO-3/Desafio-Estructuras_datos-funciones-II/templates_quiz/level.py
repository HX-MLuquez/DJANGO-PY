def choose_level(n_pregunta, p_level):
      #               1    ,     2
    # Construir lógica para escoger el nivel
    ##################################################
    pass
    #                                                          1   2       2             3    4        4         5   6 
    # * Ejemplo:  Dado que seleccionamos p_level -> 2      n_pregunta <= p_level   |  n_pregunta <= 2*p_level   else
    #                 *   n_pregunta 1 -> 'basicas'   n_pregunta 2 -> 'basicas'
    #                 *   n_pregunta 3 -> 'intermedias'   n_pregunta 4 -> 'intermedias'
    #                 *   n_pregunta 5 -> 'avanzadas'   n_pregunta 6 -> 'avanzadas'
    
    ##################################################
    
    """
    1  -  2        n_pregunta <= p_level       'basicas' 
    
    2  -  2        n_pregunta <= p_level       'basicas' 
    
    3  -  4       n_pregunta <= 2*p_level      'intermedias'
    
    4  -  4       n_pregunta <= 2*p_level      'intermedias'
    
    5  -  2     else:    'avanzadas'
    
    6  -  2
    
    """
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias