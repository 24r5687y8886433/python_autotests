import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN ='702b80f39d09f7eec9cf0da26a8384d2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Зазавр1",
    "photo_id": 4
}

body_pokeboll = {
    "pokemon_id": "43203"
}

response_create  = requests.post(url = f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)

boby_change = {
    
    "pokemon_id": "43203",
    "name": "New Namme",
    "photo_id": 2

}
messange= response_create.json()['messange']
print(messange)


'''response_change = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= boby_change)
print(response_change.json)'''

