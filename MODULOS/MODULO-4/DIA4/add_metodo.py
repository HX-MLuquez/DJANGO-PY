
# todo: Sobrecarga

class Dato:
    def __init__(self, dato1):
        self.dato1 = dato1


dato1 = Dato(10)
dato2 = Dato(30)
print(dato1)

# print(dato1 + dato2) #! TypeError: unsupported operand type(s) for +: 'Dato' and 'Dato'


class Info:
    def __init__(self, dato1):
        self.dato1 = dato1

    def __str__(self) -> str:
        return f'{self.dato1}'

    # __add__         suma_info <- 
    def __add__(self, suma_info):
        return Info(self.dato1 + suma_info.dato1)


info1 = Info(12) # --> <__main__.Dato object at 0x00000220ED66AD50> <-- 12
info2 = Info(22)
info3 = Info(130)
print(info1 + info2 + info3) # 164
