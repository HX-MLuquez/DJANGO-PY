from te import Te 



mi_te = Te() # <- OBJETO

sabor = input("Ingrese sabor: \n 1. Te negro \n 2. Te verde \n 3. Agua de hierbas\n > ")

min, recom, sabor_selec = Te.tiempo_y_recomendacion(sabor)

gramos = int(input("Ingrese formato en gramos: \n 300 \n 500 \n > "))

precio = Te.precio(gramos)

print(f'''El pedido es un {sabor_selec} en formato de {gramos} gr, 
      con un valor de ${precio}, en {min} minutos de preparación y recomendamos tomar {recom}''')