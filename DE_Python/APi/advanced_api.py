import requests
import json


def GetPokemon():
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon'

    record_count = requests.get(pokemon_url).json().get('count')

    all_data = []

    for i in range(0, record_count, 20):
        paginated_url= f'{pokemon_url}?offset={i}&limit=20'
        paginated_res = requests.get(paginated_url)
        data = paginated_res.json()
        all_data.append(data)

    with open('DE_Python/APi/pokemon_json', 'w') as f:
        json.dump(all_data, f, indent=4)


def main():
    GetPokemon()


if __name__ == '__main__':
    main()