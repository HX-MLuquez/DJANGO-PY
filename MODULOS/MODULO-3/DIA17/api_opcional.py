#* END-POINT único https://reqres.in/api/users

import requests 
import json 

def req(type, url, data={}):
    return json.loads(requests.request(type,url=url, data=data).text)

lista_usuarios = req("GET", "https://reqres.in/api/users")


#* POST - Crear  -> {"title":"", id:23} -> req("POST", "https://reqres.in/api/users", data={"title":"", id:23})

#* PUT - Actualizar -> {"first_name":"Pepe"} <- ID ¿Cual usuario UPDATE? -> req("PUT", f'https://reqres.in/api/users/{ID}', data={"first_name":"Pepe"})

#* DELETE - Eliminar -> ID ¿Cual usuario ELIMINAR? -> req("DELETE", f'https://reqres.in/api/users/{ID}')

print(lista_usuarios["data"])

# https://reqres.in/api/users/1 <- PUT DELETE

eliminar = requests.delete("https://reqres.in/api/users/5")

print(eliminar)

"""
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
      "id": 1,
      "email": "george.bluth@reqres.in",
      "first_name": "George",
      "last_name": "Bluth",
      "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    {
      "id": 2,
      "email": "janet.weaver@reqres.in",
      "first_name": "Janet",
      "last_name": "Weaver",
      "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    {
      "id": 3,
      "email": "emma.wong@reqres.in",
      "first_name": "Emma",
      "last_name": "Wong",
      "avatar": "https://reqres.in/img/faces/3-image.jpg"
    },
    {
      "id": 4,
      "email": "eve.holt@reqres.in",
      "first_name": "Eve",
      "last_name": "Holt",
      "avatar": "https://reqres.in/img/faces/4-image.jpg"
    },
    {
      "id": 5,
      "email": "charles.morris@reqres.in",
      "first_name": "Charles",
      "last_name": "Morris",
      "avatar": "https://reqres.in/img/faces/5-image.jpg"
    },
    {
      "id": 6,
      "email": "tracey.ramos@reqres.in",
      "first_name": "Tracey",
      "last_name": "Ramos",
      "avatar": "https://reqres.in/img/faces/6-image.jpg"
    }
  ],
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
"""