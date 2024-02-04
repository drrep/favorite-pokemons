import logging
import random
import sys
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .db import database, insert_pokemons, get_pokemons
from .pokeapi import fetch_pokemons

FAVORITE_POKEMONS = ["lapras", "charizard", "articuno", "blastoise", "swellow",
                     "ninetales", "cyndaquil", "arcanine", "entei", "lugia",
                     "totodile", "eevee", "nidoking", "pidgeot", "ampharos"]

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

templates = Jinja2Templates(directory="./src/templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="./src/static"), name="static")

@app.on_event("startup")
async def startup():
    await database.connect()
    poke = await fetch_pokemons(FAVORITE_POKEMONS)
    await insert_pokemons(poke)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root(request: Request):
    pokemons = await get_pokemons()
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "pokemons": random.sample(pokemons, 3)})
