
#TODO: ZIP
prefijo= ["La", "el", "la"]
frutas = ["pera", "ananá", "banana"]
perros = ["doberman", "dogman", "boby"]

print(zip(prefijo, frutas)) # <zip object at 0x000001D4DF2D0D40>

print(list(zip(prefijo, frutas, perros))) # [('La', 'pera', 'doberman'), ('el', 'ananá', 'dogman'), ('la', 'banana', 'boby')]

for primera, segunda, tercera  in zip(prefijo, frutas, perros):
     print(f' primera -> {primera} - segunda {segunda} - tercera {tercera}')
     
# Tomamos dos listas y las pasamos a un dict

diccionario = dict(zip(prefijo, frutas))
print(f'Diccionario ---> {diccionario}') # ---> {'La': 'pera', 'el': 'ananá', 'la': 'banana'}