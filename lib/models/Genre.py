class Genre:
    all = [] 
    def __init__(self, name):
        self.name = name
    
        self._platforms = []
        self._games = []
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 0 < len(name) and hasattr(self,"name"):
            self._name = name
        else:
            raise Exception("The name must be a string and have more than 0 characters")

        
    def add_game(self):
        return self._games
    
    def add_platform(self):
        return self._platforms