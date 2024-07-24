
class Resta:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return f'{self.value}'
    
    def __sub__(self, otro):
        return Resta(self.value - otro.value)
    

test1 = Resta(54)
print(test1) # -> 54

test2 = Resta(21)

resultado = test1 - test2 

print(resultado) # -> 33
