import requests

token = '7f98023761a246726db06eecb07cf32b'
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg',json = {
    "trainer_token": token,
    "email": "kostayyqa@dolnikov.ru",
    "password": "Iloveqa1"
}, headers = {'Content-Type':'application/json'})

print(response.text)

response_activation = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token
}, headers = {'Content-Type':'application/json'})

print(response_activation.text)

response_pokemons = requests.post(f'{host}/pokemons', json = {
    "name": "luma",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type':'application/json','trainer_token': token})

print(response_pokemons.text)

response_pokemons = requests.post(f'{host}/pokemons', json = {
    "name": "puma",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type':'application/json','trainer_token': token})

print(response_pokemons.text)

response_change_pokemons = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5618",
    "name": "zuma",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"

}, headers = {'Content-Type':'application/json','trainer_token': token})

print(response_change_pokemons.text)

response_add_pokemons = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "5618"

}, headers = {'Content-Type':'application/json','trainer_token': token})

print(response_add_pokemons.text)

