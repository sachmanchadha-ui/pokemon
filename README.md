#now make a get request to the api to get the information stored in the api and then store it in a variable called response 

`response=requests.get(url)`

#print the information received by the api in json() format 

`print(response.json())`

**NOW INORDER TO FETCH SPECIFIC DATA (EX. STATS OF A POKÉMON)**

#Import the module named requests 

`import requests`

#take a user input from the user (choosing POKÉMON)

`pokémon_name=input(“name of the pokémon you want to choose”)`

#save the url in a variable 

`url=f“[https://pokeapi.co/api/v2/pokemon/](https://pokeapi.co/api/v2/pokemon/pikachu){pokemon_name}”`

NOTE: f string is used to insert a value into a string 

#now make a get request to the api to get the information stored in the api and then store it in a variable called response 

`response=requests.get(url)`

#store the response.json() into data 

`data=response.json()` 

#print the stats of pokemon using dictionaries 

`print(“name”,data[“name ”])`

`print(“height”,data[“height”])`

`print(“weight”,data[“weight”])`

#it can also be printed using f string inorder to print them in a structured format

`Name=data[name]`

`type=data[types][0][type][name]`

NOTE: type in the api is a list like this:

{
  "types": [
    {
      "slot": 1,
      "type": {
        "name": "electric"
      }
    },
    {
      "slot": 2,
      "type": {
        "name": "flying"
      }
    }
  ]
}
NOTE:look at this like:

data (dict)
└── "types" (list)
└── [0] (dict)
└── "type" (dict)
└── "name" (string)

`Height=data[height]`

`Weight=data[weight]`

`print(f”Name:{name}”)`

`print(f”Type:{type}”)`

`print(f”Height:{height}”)`

`print(f”Weight:{weight}”)`
