
# TODO: REQUEST and RESPONSE API-REST

# * END POINT
# Direcciones (urls específicas)  a fin de acceder o hacer diferentes acciones en un Servidor
# API-Rest
# https://rickandmortyapi.com/api/character

import requests
import json
# pip install requests

url_principal = 'https://rickandmortyapi.com/api'


print(f'{url_principal}/character')

payload = {}
headers = {}

# * ESTAMOS haciendo una petición a un end-point específico de una API free
#          verbo o método -> GET dejame VER  -  la url es el <- end-point
response = requests.request(
    "GET", "https://rickandmortyapi.com/api/character", headers=headers, data=payload)

print(response)  # <Response [200]>
# print(response.text) # super string de toda la info que nos brinda ese end-point

result = json.loads(response.text)  # -> Pasa a tipo de dato real adecuado
# print(result["results"][1])

for character in result["results"]:
    print(character["name"], character["image"])


"{'nombre':'Mau'}"
# ->
{"nombre": "Mau"}

"[{'nombre':'Mau'},{'nombre':'Pepe'},{'nombre':'José'}]"  # * STRING
# ->
[{'nombre': 'Mau'}, {'nombre': 'Pepe'}, {'nombre': 'José'}]

print("---------------------------------------------------------------")


def req_get_all_episodes(url):
    result = json.loads(requests.get(url).text)
    return result["results"]


url_episode = f'{url_principal}/episode'

episodios = req_get_all_episodes(url_episode) # -> [{},{},{}, ... ...,{}]

# print(episodios)

for epi in episodios:
    print(epi["name"])
    

print("----------------------- POSTMAN ----------------------------------------")

def get_all_posts(url):
    result = json.loads(requests.get(url).text)
    return result
# print(get_all_posts("https://jsonplaceholder.typicode.com/posts")[0:10])

def get_post_by_id(url, id):
    result = json.loads(requests.get(f'{url}/{id}').text)
    return result
    
print(get_post_by_id("https://jsonplaceholder.typicode.com/posts", "2"))


# print(get_post_by_id("https://jsonplaceholder.typicode.com/posts", "31"))


# Piden los datos del Usuario que realizó el posteo id 31

posteo31 = get_post_by_id("https://jsonplaceholder.typicode.com/posts", "31")

print(posteo31["userId"]) # gracias al posteo encontré el ID del user

def get_user_by_id(url, id):
    result = json.loads(requests.get(f'{url}/{id}').text)
    return result

usuario_que_posteo31 = get_user_by_id("https://jsonplaceholder.typicode.com/users", str(posteo31["userId"]))
print(usuario_que_posteo31)


print("===============================================")

# episodios -> [{ },{ }, ... ...]
#                | -> {}.keys() -> ['id', 'name', etc...]
print(episodios[0].keys()) # dict_keys(['id', 'name', 'air_date', 'episode', 'characters', 'url', 'created'])

print(episodios[0]["name"])

print([epi["name"] for epi in episodios])


print("--------------------------- SEGURIDAD en APIS ------------------------")

def request_get(url):
    return json.loads(requests.get(f'{url}').text)
    
data_cortada = request_get('https://jsonplaceholder.typicode.com/photos')[0:10]
print(data_cortada) 