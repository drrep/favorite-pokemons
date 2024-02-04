import aiohttp
import logging
from aiostream import stream

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

logger = logging.getLogger(__name__)

async def fetch_pokemons(pokemon_names: list[str]):
    s = stream.iterate(pokemon_names)
    x = stream.map(s, fetch_pokemon, task_limit=4)
    result = await stream.list(x)
    logger.info("fetched %d pokemons", len(result))
    return list(map(_convert_pokemon_result, result))

async def fetch_pokemon(pokemon_name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(POKEAPI_BASE_URL + pokemon_name) as response:

            return await response.json()

def _convert_pokemon_result(pokemon: dict) -> dict:
    return {"name": pokemon["name"],
            "height": pokemon["height"],
            "sprite": pokemon["sprites"]["front_default"],
            "weight": pokemon["weight"]}