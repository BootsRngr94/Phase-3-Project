from models.Genre import Genre
from models.Platform import Platform
from models.Game import Game

def exit_program():
    print("Game you later!")
    exit()


def add_game(title, genre_name, platform_name):
    genre = Genre.find_by_name(genre_name)
    platform = Platform.find_by_name(platform_name)

    if not genre:
        genre = Genre.create(genre_name)
        genres.append(genre)

    if not platform:
        platform = Platform.create(platform_name)
        platforms.append(platform)

    Game.create(title, genre, platform)


        
def display_games():
    games = Game.get_all()
    
    print("")

    for game in games:  
        print(f"Title: {game.title},\n Genre: {game.genre.name},\n Platform: {game.platform.name} \n\n")


genres = []
platforms = []
games = []


def delete_game(title):
    from models.Game import Game
    uppercase = title.upper()
    game = Game.find_by_title(uppercase)
    game.delete()
    print(f'{game.title} is fin')

def find_by_title(title):
    from models.Game import Game
    uppercase = title.upper()
    # print(uppercase)
    game = Game.find_by_title(uppercase)
    print(f"Title: {game.title},\n Genre: {game.genre.name},\n Platform: {game.platform.name}")
        
    