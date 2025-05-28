import requests
import random

#Clase Pokemon
class Pokemon:
    def __init__(self, name, image_url, poke_id, moves):
        self.name = name
        self.image_url = image_url
        self.poke_id = poke_id
        self.moves = moves

#Definimos la función para buscar un pokemon
def get_random_pokemon_by_type(poke_type):
    type_url = f'https://pokeapi.co/api/v2/type/{poke_type}'
    type_data = requests.get(type_url).json()
    pokemon_list = type_data['pokemon']
    selected_pokemon = random.choice(pokemon_list)['pokemon']
    
    poke_data = requests.get(selected_pokemon['url']).json()
    name = poke_data['name'].capitalize()
    image_url = poke_data['sprites']['front_default']
    poke_id = poke_data['id']
    
    # Obtener primeros 4 ataques
    moves = poke_data['moves']
    move_names = [move['move']['name'].capitalize() for move in moves[:4]]

    return Pokemon(name, image_url, poke_id, move_names)


