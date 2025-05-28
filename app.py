from flask import Flask, render_template, request
import requests
import random

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Ruta principal: renderiza la vista principal y maneja el formulario POST
@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon_data = None  # Variable para guardar los datos del Pokémon a mostrar
    types = get_pokemon_types()  # Lista de tipos de Pokémon desde la API

    if request.method == 'POST':
        selected_type = request.form.get('type')  # Obtener tipo seleccionado en el formulario
        pokemon_data = get_random_pokemon_by_type(selected_type)  # Obtener Pokémon aleatorio del tipo

    # Renderiza la plantilla HTML pasando tipos disponibles y el Pokémon si fue generado
    return render_template('index.html', types=types, pokemon=pokemon_data)

# Función para obtener todos los tipos de Pokémon desde la PokéAPI
def get_pokemon_types():
    response = requests.get('https://pokeapi.co/api/v2/type/')
    if response.status_code == 200:
        # Retorna una lista con los nombres de todos los tipos (fuego, agua, planta, etc.)
        return [t['name'] for t in response.json()['results']]
    return []

# Función que recibe un tipo y devuelve un Pokémon aleatorio de ese tipo
def get_random_pokemon_by_type(pokemon_type):
    response = requests.get(f'https://pokeapi.co/api/v2/type/{pokemon_type}')
    if response.status_code == 200:
        all_pokemon = response.json()['pokemon']  # Lista completa de Pokémon de ese tipo
        random_pokemon = random.choice(all_pokemon)['pokemon']  # Elegimos uno al azar
        pokemon_info = requests.get(random_pokemon['url']).json()  # Obtenemos su información detallada

        # Retornamos un diccionario con los datos más relevantes
        return {
            'name': pokemon_info['name'].capitalize(),
            'id': pokemon_info['id'],
            'sprite': pokemon_info['sprites']['front_default'],
            'moves': [move['move']['name'] for move in pokemon_info['moves'][:4]]  # Primeros 4 ataques
        }

    return None  # Si hay error en la petición, devolvemos None

# Ejecutamos la app en modo debug para desarrollo
if __name__ == '__main__':
    app.run(debug=True)
