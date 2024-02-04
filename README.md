# Favorite pokemons
A small webapp which shows some my favorite pokemons randomized.
Built with FastApi server, asyncio and serverside template rendering.

## Run in virtual env
Used python version 3.10.5
```
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ ./entrypoint.sh
```

## Run in Docker

1. Build the image: `docker-compose build` or `docker build -t drep-app .`
2. Run with `docker run --rm -it -p 8000:8000 drep-app <exercise_number>` or `docker-compose up -d` (shut down with `docker-compose down`)
