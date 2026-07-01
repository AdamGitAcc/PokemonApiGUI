import variables
import requests
import variables
import requests

base_url = 'https://pokeapi.co/api/v2/type/'

def type_search(Type):
    url = f'{base_url}{Type}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        data_list = []
        for data in pokemon_data['moves']:
            data_list.append(data['name'])
        return data_list
    else:
        print(f'failed to retrieve data {response.status_code}')

