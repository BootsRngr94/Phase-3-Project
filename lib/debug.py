#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.Game import Game
from models.Genre import Genre
from models.Platform import Platform

def reset_database():
    Game.drop_table()
    Game.create_table()
    Genre.drop_table()
    Genre.create_table()
    Platform.drop_table()
    Platform.create_table()
reset_database()

RPG = Genre.create("RPG")

Xbob = Platform.create("Xbob-ultimate 1")



g1 = Game.create("DarkTide", RPG, Xbob)






ipdb.set_trace()
