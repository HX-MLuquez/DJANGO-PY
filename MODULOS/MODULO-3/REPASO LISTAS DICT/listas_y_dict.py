
mascotas = []  # [{}{}{}]

lista_mascotas = {}
lista_mascotas['nombre'] = "Lulu"
lista_mascotas['edad'] = 12

modelo_mascota = {
    "nombre": "",
    "edad": "",
    "email": "test@gmail.com",
    "raza": "",
    "vacunas": []
}
# mascotas.append(modelo_mascota)

for i in range(2):
    #TODO: modo simple
    # nombre = input("Ingrese nombre: ")
    # edad = input("Ingrese edad: ")
    # email = input("Ingrese email: ")
    # raza = input("Ingrese raza: ")
    # mascota = {
    #     "nombre": nombre,
    #     "edad": edad,
    #     "email": email,
    #     "raza": raza,
    #     "vacunas": []
    # }

    #TODO: Manera dinámica
    mascota = {}
    for k, v in modelo_mascota.items():
        mascota[k] = input(f"Ingrese {k}: ")
    mascotas.append(mascota)

print(f'Lista de mascotas: {mascotas}')

search_by_email = input("Ingrese email a buscar: ").lower()
encontrado = False
mascota_encontrada = {}
for m in mascotas:
    if m.get("email") == search_by_email:
        encontrado = True
        mascota_encontrada = m.copy()
        break
if encontrado:
    print(f"La mascota encontrada es {mascota_encontrada}")
else:
    print("lo siento")

print("fin")

# print(modelo_mascota.get("email", "No registra email de contacto"))
