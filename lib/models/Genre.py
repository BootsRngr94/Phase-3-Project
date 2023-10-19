from models.__init__ import CURSOR, CONN
class Genre:
    all = {} 
    def __init__(self, name):
        self.name = name
    
        self._platforms = []
        self._games = []
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        

        
    def add_game(self):
        return self._games
    
    def add_platform(self):
        return self._platforms
    
    @classmethod
    def create_table(cls):
            """ Create a new table to persist the attributes of Genre instances """
            sql = """
                CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY,
                name TEXT)
            """
            CURSOR.execute(sql)
            CONN.commit()
   
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Genre instances """
        sql = """
            DROP TABLE IF EXISTS genres;
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        """ Insert a new row with the name of the current Genre instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO genres (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
   

    @classmethod
    def create(cls, name):
        """ Initialize a new Genre instance and save the object to the database """
        genre = cls(name)
        genre.save()
        return genre
   
   
    def update(self):
        """Update the table row corresponding to the current Genre instance."""
        sql = """
            UPDATE genres
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()


    def delete(self):
        """Delete the table row corresponding to the current Genre instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM genres
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
       
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        """Return a Genre object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        genre = cls.all.get(row[0])
        if genre:
            genre.name = row[1]
        else:
            genre = cls(row[1])
            genre.id = row[0]
            cls.all[genre.id] = genre
        return genre


    @classmethod
    def find_by_id(cls, id):
        """Return a Genre object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM genres
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Genre object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM genres
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    