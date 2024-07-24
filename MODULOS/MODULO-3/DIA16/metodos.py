
import requests
import json

# TODO: VERBOS - MÉTODOS

# * GET <- Obtener
# * POST <- CREAR
# * PUT <- ACTUALIZAR
# * DELETE <- ELIMINAR
url = "https://jsonplaceholder.typicode.com/posts"


def req_put_post(url, id, data):
    return json.loads(requests.put(f'{url}/{id}', json=data).text)


posteo_nueva_info = {"title": "Hola mundo API"}

print(req_put_post(url, "4", posteo_nueva_info))

# -> {'title': 'Hola mundo API', 'id': 4}


def req_post_post(url, data):
    return json.loads(requests.post(f'{url}', json=data).text)


posteo_nuevo = {
    "userId": 101,
    "id": 403,
    "title": "HI",
    "body": "jujuju"
},

print(req_post_post(url, posteo_nuevo))
# -> {'0': {'userId': 101, 'id': 403, 'title': 'HI', 'body': 'jujuju'}, 'id': 101}


def req_delete_post(url, id):
    return json.loads(requests.delete(f'{url}/{id}').text)

print(req_delete_post(url, "3"))
#-> {}


posteo_nuevo = '''{
    "userId": 101,
    "id": 403,
    "title": "HI",
    "body": "jujuju"
}'''
requests.post(f'{url}', data=posteo_nuevo).text
