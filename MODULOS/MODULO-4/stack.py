

class Stack:
    
    def __init__(self) -> None:
        self.list_user= []
        self.index=0
    def add(self, nombre, edad):
        user={
            "id": self.index,
            "nombre": nombre,
            "edad": edad,
            "active": True
        }
        self.list_user.append(user)
        self.index += 1
        return user
    def eliminar(self):
        user = self.list_user.pop()
        self.index -= 1
        return user
    
    def user_activos(self):
        list_filter = [u for u in self.list_user if u["active"]== True]
        return list_filter
    def banear(self, index):
        self.list_user[index]["active"] = False 
        return  self.list_user[index]

lista_usuarios = Stack()
lista_usuarios.add("Manolo", 32)
lista_usuarios.add("Juan", 1)

print(lista_usuarios.list_user)

lista_usuarios.eliminar()
print(lista_usuarios.list_user)

lista_usuarios.add("Hulk", 331)

lista_usuarios.add("Superman", 121)

print(lista_usuarios.user_activos())

lista_usuarios.banear(2)

print(lista_usuarios.user_activos())