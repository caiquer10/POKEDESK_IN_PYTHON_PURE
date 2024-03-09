import requests
import uuid

print('PokeAPI\n')


def get_pokemon_info(pokemon):
    pokemon = pokemon.lower()  # muda letras maiusculas para minuscula, assim, pokeai reconhece o input
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)

    if response.status_code == 200 and response.text.strip():
        data = response.json()
        return {
            'id': data["id"],
            'name': data["name"],
            'weight': data["weight"],
            'height': data["height"]
        }
    else:
        print(f'Não foi possível encontrar o Pokémon {pokemon}!\n')
        return None


def create_pokemon_team():
    team = []
    while True:
        pokemon = input(
            'Digite o nome do Pokémon para adicionar na pokebola|(ou "sair" para ver todos pokemons adicionados): ')
        if pokemon.lower() == 'sair':
            break
        pokemon_info = get_pokemon_info(pokemon)
        if pokemon_info:
            team.append(pokemon_info)
            print(
                f'ID: {pokemon_info["id"]}, Nome: {pokemon_info["name"]}, Peso: {pokemon_info["weight"]}, Altura: {pokemon_info["height"]}\n')

    team_id = str(uuid.uuid4())
    print(f'\nTime de Pokémon criado com ID: {team_id}\n')
    for pokemon in team:
        print(
            f'ID: {pokemon["id"]}, Nome: {pokemon["name"]}, Peso: {pokemon["weight"]}, Altura: {pokemon["height"]}\n')


create_pokemon_team()
