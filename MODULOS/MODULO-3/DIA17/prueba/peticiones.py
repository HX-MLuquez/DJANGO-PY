
import requests
import json 

def req(url):
    response = json.loads(requests.get(url).text)
    print(response[0]["images"]["main"])

print("")