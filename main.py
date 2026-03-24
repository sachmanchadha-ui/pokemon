import requests 
pokemon_name=input("enter the name of the pokemon:")
url=f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
response=requests.get(url)
data=response.json()
Type=data["types"][0]["type"]["name"]
Height=data["height"]
weight=data["weight"]
print(f"Type:{Type}")
print(f"Height:{Height}")
print(f"Weight:{weight}")