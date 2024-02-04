import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from .models import Pokemon, Base

DATABASE_URL = "sqlite:///./src/pokemon.db"

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


async def get_pokemons():
    return await database.fetch_all(sqlalchemy.select([Pokemon]))

async def insert_pokemons(pokemons: list[dict]):
    query = sqlalchemy.insert(Pokemon)
    await database.execute_many(query, pokemons)