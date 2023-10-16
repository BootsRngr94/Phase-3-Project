class Game:
    def __init__(self, title, genre, platform):
        self.title = title
        self.genre = genre
        self.platform = platform

        genre.add_game(self)
        platform.add_game(self)