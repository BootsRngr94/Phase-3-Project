from models.__init__ import CURSOR, CONN
class Platform:
    all={}
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
    
    @classmethod
    def create_table(cls):
            """ Create a new table to persist the attributes of Platform instances """
            sql = """
                CREATE TABLE IF NOT EXISTS platforms (
                id INTEGER PRIMARY KEY,
                name TEXT)
            """
            CURSOR.execute(sql)
            CONN.commit()
   
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Platform instances """
        sql = """
            DROP TABLE IF EXISTS platforms;
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        """ Insert a new row with the name of the current Platform instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO platforms (name)
            VALUES (?)
        """


        CURSOR.execute(sql, (self.name,))
        CONN.commit()


        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
   
    @classmethod
    def create(cls, name):
        """ Initialize a new Platform instance and save the object to the database """
        platform = cls(name)
        platform.save()
        return platform
   
    def update(self):
        """Update the table row corresponding to the current Platform instance."""
        sql = """
            UPDATE platforms
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()


    def delete(self):
        """Delete the table row corresponding to the current Platform instance,
        delete the dictionary entry, and reassign id attribute"""


        sql = """
            DELETE FROM platforms
            WHERE id = ?
        """


        CURSOR.execute(sql, (self.id,))
        CONN.commit()


        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]


        # Set the id to None
        self.id = None