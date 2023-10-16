class Genre: 
    def __init__(self, name):
        self.name = name 
        self.games = []
        
    def add_game(self, game):
        self.games.append(game)