
import json
from string import Template
from peticiones import convertir, request_get
from templates import get_esqueleto, get_img_template



response = request_get("https://aves.ninjas.cl/api/birds", 30)
list_pajaros = convertir(response)
# print(json.dumps(list_pajaros, sort_keys=True, indent=2))

img_template = get_img_template()
divs = ''
for item in list_pajaros:
    divs += img_template.substitute(
        url = item["url"],
        name = item["name"],
        name2= item["name2"],
        id= item["id"]
    ) +'\n'

esqueleto = get_esqueleto()
html = esqueleto.substitute(body = divs)

with open('index.html', 'w') as f:
    f.write(html)