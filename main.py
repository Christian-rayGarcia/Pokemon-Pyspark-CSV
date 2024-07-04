from data_extraction import DataExtraction
import requests


def process_pokemon_base_data(pokemon_base_info):
	pokemon_type = [result['type']['name'] for result in pokemon_base_info['types']]
	return {
		"Index": pokemon_base_info["id"],
		"Name": pokemon_base_info["name"],
		"Type": " ".join(pokemon_type)
	}


def process_pokemon_species_data(pokemon_species_info):
	return {
		"Index": pokemon_species_info["id"],
		"IsLegendary": pokemon_species_info["is_legendary"],
		"IsMythical": pokemon_species_info["is_mythical"]
	}


def process_pokemon_stats_data(pokemon_stats_info):
	stats = ["hp", "speed", "defense", "attack", "special-attack", "special-defense"]
	stats_numerical = []

	for pokemon in pokemon_stats_info["stats"]:
		if pokemon["stat"]["name"] in stats:
			stats_numerical.append(pokemon["base_stat"])

	return {
		"Index": pokemon_stats_info["id"],
		"hp": stats_numerical[0],
		"speed": stats_numerical[1],
		"defense": stats_numerical[2],
		"attack": stats_numerical[3],
		"Sp. Atk": stats_numerical[4],
		"Sp. Def": stats_numerical[5]

	}


# base_url = "https://pokeapi.co/api/v2/"
# endpoint = "pokemon"
# output_file = "pokemon_base_data.csv"

# fetcher = DataExtraction(base_url, endpoint, process_pokemon_base_data, output_file)
# fetcher.get_data()

# species_url = "https://pokeapi.co/api/v2/"
# species_endpoint = "pokemon-species"
# species_output_file = "pokemon_species_data.csv"

# get_spiecies_data = DataExtraction(species_url, species_endpoint, process_pokemon_species_data, species_output_file)
# get_spiecies_data.get_data()


base_url = "https://pokeapi.co/api/v2/"
endpoint = "pokemon"
output_file = "pokemon_stats_data.csv"

get_stats_data = DataExtraction(base_url, endpoint, process_pokemon_stats_data, output_file)
get_stats_data.get_data()
