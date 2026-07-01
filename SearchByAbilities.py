import variables
import requests

base_url = 'https://pokeapi.co/api/v2/ability/'

def ability_search(Name):
    url = f'{base_url}{Name}'
    
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        data_list = []
        if not data_list:
            for entry in pokemon_data['effect_entries']:
                if entry['language']['name'] == 'en':
                    data_list.append(entry['short_effect'])
        return data_list
    else:
        print(f'failed to retrieve data {response.status_code}')
