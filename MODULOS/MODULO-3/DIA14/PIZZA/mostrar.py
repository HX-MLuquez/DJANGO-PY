def mostrar_ingredientes(ingredientes_orden):
    print(f'Su masa es {ingredientes_orden["masa"]}')
    print(f'Su salsa es {ingredientes_orden["salsa"]}')
    print(f'Ingredientes: ')
    for i in ingredientes_orden['ingredientes']:
        print(i)
        
if __name__ == '__main__':
    ingredientes_orden = {'masa': 'Masa Tradicional',
                      'salsa': 'Salsa de Tomate',
                      'ingredientes': ['Queso', 'Jamón']
                      }
    mostrar_ingredientes(ingredientes_orden)