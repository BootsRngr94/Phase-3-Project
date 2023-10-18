from models.Genre import Genre
from models.Platform import Platform
from models.Game import Game

def exit_program():
    print("Game you later!")
    exit()


def add_game(title, genre_name, platform_name):
    # genre = next((g for g in genres if g.name == genre_name), None)
    # platform = next((p for p in platforms if p.name == platform_name), None)
    genre = Genre.find_by_name(genre_name)
    platform = Platform.find_by_name(platform_name)

    if not genre:
        genre = Genre.create(genre_name)
        genres.append(genre)


    if not platform:
        platform = Platform.create(platform_name)
        platforms.append(platform)


    game = Game.create(title, genre, platform)
    
    #games.append(game)


        
def display_games():
    games = Game.get_all()
    import ipdb 
    ipdb.set_trace()
    
    
    for game in games:
        # if not game.genre.name or not game.platform.name: 
        #     ipdb.set_trace()   
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
