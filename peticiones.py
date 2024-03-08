import requests
import json

def request_get(url,cantidad):
    return json.loads(requests.get(url).text)[:cantidad]

"""[
    
        url: ''
        nombre: '' 
        name: ''
    },
        {
        url: ''
        nombre: '' 
        name: ''
    }
]"""
def convertir(lista_pajaros):
    return [{
        "url":elem["images"]["main"],
        "name":elem["name"]["spanish"],
        "name2":elem["name"]["english"],
        "id": elem["uid"]
        } for elem in lista_pajaros
    ]
