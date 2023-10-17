class Game:

    all = []
    def __init__(self, title, genre, platform):
        self.title = title
        self.genre = genre
        self.platform = platform

        Game.all.append(self)
    
        self.genre._games.append(self)
        self.genre._platforms.append(self.platform)

        self.platform._games.append(self)
        self.platform._genres.append(self.genre)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str and 0 < len(title) and not hasattr(self,"title"):
            self._title = title
        else:
            raise Exception("The title must be a string and have more than 0 characters")
        
   

   
    
        