from models.__init__ import CURSOR, CONN


class Game:


    all = {}
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
       
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, genre):
        if type(genre) == str and 0 < len(genre) and not hasattr(self,"genre"):
            self._genre = genre
        else:
            raise Exception("The genre must be a string and have more than 0 characters")
       
    @property
    def platform(self):
        return self._platform
    @platform.setter
    def platform(self, platform):
        if type(platform) == str and 0 < len(platform) and not hasattr(self,"platform"):
            self._platform = platform
        else:
            raise Exception("The platform must be a string and have more than 0 characters")
       
    @classmethod
    def create_table(cls):
            """ Create a new table to persist the attributes of Game instances """
            sql = """
                CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY,
                title TEXT,
                genre TEXT,
                platform TEXT)
            """
            CURSOR.execute(sql)
            CONN.commit()
   
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Game instances """
        sql = """
            DROP TABLE IF EXISTS games;
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        """ Insert a new row with the title, genre, and platform of the current Game instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO games (title, genre, platfrom)
            VALUES (?, ?, ?)
        """


        CURSOR.execute(sql, (self.title, self.genre, self.platform))
        CONN.commit()


        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
   
    @classmethod
    def create(cls, title, genre, platform):
        """ Initialize a new Game instance and save the object to the database """
        game = cls(title, genre, platform)
        game.save()
        return game
   
    def update(self):
        """Update the table row corresponding to the current Game instance."""
        sql = """
            UPDATE games
            SET title = ?, genre = ?, platform = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.genre, self.platform, self.id))
        CONN.commit()


    def delete(self):
        """Delete the table row corresponding to the current Game instance,
        delete the dictionary entry, and reassign id attribute"""


        sql = """
            DELETE FROM games
            WHERE id = ?
        """


        CURSOR.execute(sql, (self.id,))
        CONN.commit()


        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]


        # Set the id to None
        self.id = None
