class Platform:
    def __init__(self, name):
        self.name = name
        self._games = []
        self._genres = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if type(name) == str and 0 < len(name) and not hasattr( self, "name"):
            self._name = name
        else:
            raise Exception("The name must be a string and have more 0 characters")
    
    def add_(self):
        return self._genres

    def add_game(self):
        return self._games