
#todo_ Colaboración - agregación normal ---  son INDEPENDIENTES
class Motor:
    def arrancar(self):
        print("El motor se ha encendido")

# motor4 = Motor()
# motor4.arrancar() #    "El motor se ha encendido"

class Coche:
    def __init__(self, motor: Motor) -> None:
        self.motor = motor  #  Objeto instanciado ya ->  motor1 
    def encender(self):
        self.motor.arrancar()
        print("El coche está listo")

motor1 = Motor() # Objeto motor1 

coche1 = Coche(motor1) # El motor se ha encendido
coche1.encender() # El coche está listo 


del coche1 
print(motor1) # <__main__.Motor object at 0x0000022D3EC8AA20>
print(coche1) #! NameError: name 'coche1' is not defined

coche22 = Coche(motor1)


