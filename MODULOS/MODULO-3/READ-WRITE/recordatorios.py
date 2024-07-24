lista = [['2021-01-01', '11:00', {"titulo": 'Levantarse y ejercitar', "id": "123", "invitados":["Jose", "Pedro"]}],  
['2021-01-02', '06:00', {"titulo": 'Empezar el año', "id": "123", "invitados":["Jose", "Pedro"]}],  
['2021-07-16', '13:00', {"titulo": 'No hacer nada es feriado', "id": "123", "invitados":["Jose", "Pedro"]}],  
['2021-09-18', '16:00', {"titulo": 'Ramadas', "id": "123", "invitados":["Jose", "Pedro"]}],  
['2021-12-24', '22:00', {"titulo": 'Cena de Navidad', "id": "123", "invitados":["Jose", "Pedro"]}],  
['2021-12-25', '00:00', {"titulo": 'Navidad', "id": "123", "invitados":["Jose", "Pedro"]}],  
['2021-12-31', '22:00', {"titulo": 'Cena de Año Nuevo', "id": "123", "invitados":["Jose", "Pedro"]}]] 

lista[0][1] = "15:00" # <- ['2021-01-01', '11:00', 'Levantarse y ejercitar']
# lista.insert(2, ["hola"])
# lista.append("final")
# lista.append("final")
# lista.pop()
# lista.pop(1)
print(lista)

print(lista[6][2]["invitados"])

for i in lista[6][2]["invitados"]:
    print(i)