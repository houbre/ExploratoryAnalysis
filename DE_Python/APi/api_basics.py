import requests
import json


def GetPokemon():
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon'

    response = requests.get(pokemon_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception('Error while fetching the data')


def main():
    data = GetPokemon()
    print(data)


if __name__ == '__main__':
    main()