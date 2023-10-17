from models.__init__ import CURSOR, CONN


class Game:


    all = {}
    def __init__(self, title, genre, platform):
        self.title = title
        self.genre = genre
        self.platform = platform


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
        from models.Genre import Genre
        if  isinstance(genre, Genre) and not hasattr(self,"genre"):
            self._genre = genre
        else:
            raise Exception("The genre must be an instance of a Genre")
       
    @property
    def platform(self):
        return self._platform
    @platform.setter
    def platform(self, platform):
        from models.Platform import Platform
        if isinstance(platform, Platform) and not hasattr(self,"platform"):
            self._platform = platform
        else:
            raise Exception("The platform must be an instance of Platform")
       
    @classmethod
    def create_table(cls):
            """ Create a new table to persist the attributes of Game instances """
            sql = """
                CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY,
                title TEXT,
                genre INTEGER,
                platform INTEGER)
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
            INSERT INTO games (title, genre, platform)
            VALUES (?, ?, ?)
        """
        # import ipdb; ipdb.set_trace()

        CURSOR.execute(sql, (self.title, self.genre.id, self.platform.id))
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

    @classmethod
    def instance_from_db(cls, row):
        """Return a Game object having the attribute values from the table row."""
        from models.Platform import Platform
        from models.Genre import Genre

        # Check the dictionary for an existing instance using the row's primary key
        
        genre = Genre.find_by_id(row[2])
        platform = Platform.find_by_id(row[3])

        game = cls.all.get(row[0])
        if game:
            # ensure attributes match row values in case local instance was modified
            game.title = row[1]
            game.genre = row[2]
            game.platform = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary

            game = cls(row[1], genre, platform)
            game.id = row[0]
            cls.all[game.id] = game
        return game

    @classmethod
    def get_all(cls):
        """Return a list containing a Game objects per row in the table"""
        sql = """
            SELECT *
            FROM games
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
