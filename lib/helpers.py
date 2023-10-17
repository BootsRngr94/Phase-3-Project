from models.Genre import Genre
from models.Platform import Platform
from models.Game import Game

def add_game(title, genre_name, platform_name):
    genre = next((g for g in genres if g.name == genre_name), None)
    platform = next((p for p in platforms if p.name == platform_name), None)

    if not genre:
        genre = Genre(genre_name)
        genres.append(genre)

    if not platform:
        platform = Platform(platform_name)
        platforms.append(platform)

    game = Game(title, genre, platform)
    games.append(game)

def display_games():
    for game in games:
        print(f"Title: {game.title}, Genre: {game.genre.name}, Platform: {game.platform.name}")

genres = []
platforms = []
games = []

def delete_game(title):
    game = next((g for g in games if g.title == title), None)

    if game:
        game.genre.games.remove(game)
        game.platform.games.remove(game)
        games.remove(game)
    else:
        print(f"No game found with title '{title}'")

