import requests

base_url = "https://pokeapi.co/api/v2/"


def get_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"{response.status_code} was Filed!!!")


pokemon_name = 'ditto'

pokemon_info = get_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info['name']}")
    print(f"{pokemon_info['id']}")
    print(f"{pokemon_info['height']}")
    print(f"{pokemon_info['base_experience']}")
