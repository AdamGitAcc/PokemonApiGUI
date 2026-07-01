import variables
import requests

base_url = 'https://pokeapi.co/api/v2/pokemon/'

def name_search(Ability):
    url = f'{base_url}{Ability}'
    
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        data_list = [f'Name: {pokemon_data['name']}', f'Weight: {pokemon_data['weight']}', f'Height: {pokemon_data['height']}']
        return data_list
    else:
        print(f'failed to retrieve data {response.status_code}')

