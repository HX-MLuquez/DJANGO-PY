"""
Ejercicio 1:
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos 
el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""


class Alumno:
    def __init__(self, nombre: str, nota: int) -> None:
        self.nombre = nombre
        self.nota = nota

    def __str__(self) -> str:
        return f'nombre: {self.nombre} - nota: {self.nota}'

    def resultado(self):
        if self.nota >= 7:
            print(f"Con resultado {self.nota} ha aprobado")
        else:
            print(f"Con resultado {self.nota} ha desaprobado")


alumno1 = Alumno("Toto", 3)
alumno2 = Alumno("Manolo", 7)

print(alumno1)
print(alumno2)

alumno1.resultado()
alumno2.resultado()
