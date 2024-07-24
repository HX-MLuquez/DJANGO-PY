import requests 
import json 

# End-point https://aves.ninjas.cl/api/birds

def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ == "__main__":
    response = request_get("https://aves.ninjas.cl/api/birds")
    # print(response)
    print(len(response))
    for p in response:
        print(p["_links"]["self"])
    
"""
[{},{},{},{},{} - 216]

    {
        "uid": "76-buteo-albigula",
        "name": {
            "spanish": "Aguilucho Chico",
            "english": "White-throated Hawk",
            "latin": "Buteo albigula"
        },
        "images": {
            "main": "https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.200x0.jpg",
            "full": "https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.jpg",
            "thumb": "https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.200x0.jpg"
        },
        "_links": {
            "self": "https://aves.ninjas.cl/api/birds/76-buteo-albigula",
            "parent": "https://aves.ninjas.cl/api/birds"
        },
        "sort": 0
    },
"""