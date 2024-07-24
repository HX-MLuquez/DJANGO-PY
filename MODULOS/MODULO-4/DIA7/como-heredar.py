


class Padre:
    def __init__(self) -> None:
        pass
    def met(self):
        print("q")
        
class Hija(Padre):
    def __init__(self) -> None:
        super().__init__()
        
    def met(self):
        # super().met()
        pass