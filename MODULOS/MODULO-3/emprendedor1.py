# """"
# # U𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺𝑇
# Donde:
# P: Precio de Suscripción
# U: Número de Usuarios
# GT: Gastos Totales
# """
# Para ello utiliza input() para solicitar
# como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
# print("probando")

p = float(input('Ingrese el Precio de Suscripción: '))
u = float(input('Ingrese el número de Usuarios: '))
gt = float(input('Ingrese los gastos totales: '))

utilidades = p * u - gt

print(f'Las utilidades son: {utilidades:.2f}')
