import matplotlib.pyplot as plt
import matplotlib.image as img
import requests
pokemon =input("Introduce el nombre de tu pokemon: ")
url= "https://pokeapi.co/api/v2/pokemon/" + pokemon
res= requests.get(url)

if res.status_code !=200 :
    print("pokemon no encontrado")
    exit()

imagen = img.imread(res.json()['sprites']['front_default'])
plt.title(res.json()['name'])
imgplot = plt.imshow(imagen)
plt.show()