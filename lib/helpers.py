from models.Genre import Genre
from models.Platform import Platform
from models.Game import Game

def exit_program():
    print("Game you later!")
    exit()


def add_game(title, genre_name, platform_names):
    genre = Genre.find_by_name(genre_name)
    
    if not genre:
        genre = Genre.create(genre_name)
        genres.append(genre)

    
    existing_game = Game.find_by_title(title.upper())
    
    if existing_game:
        print("Game already exists in this list!")
   
    platforms = []
    for platform_name in platform_names:
        platform = Platform.find_by_name(platform_name)
        
    if not platform:
        platform = Platform.create(platform_name)
        platforms.append(platform)

    else:
        platforms.append(platform)
    Game.create(title, genre, platform)
    return True    


        
def display_games():
    games = Game.get_all()
    
    print("")

    for game in games:  
        print(f"Title: {game.title}\nGenre: {game.genre.name}\nPlatform: {game.platform.name} \n\n")


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
    try:
        game = Game.find_by_title(uppercase)
        if game is not None:
            print(f"Title: {game.title}\nGenre: {game.genre.name}\nPlatform: {game.platform.name}")
        else:
            print(f"No game found with the title: {title}")
    except Exception as e:
        raise Exception(f"Error finding game: {e}")  
    
    