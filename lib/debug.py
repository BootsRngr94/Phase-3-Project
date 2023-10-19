#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
# import ipdb
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

action = Genre.create("Action")
platform = Genre.create("Platform")
shooter = Genre.create("Shooter")
fighter = Genre.create("Fighter")
race = Genre.create("Race")
rhythm = Genre.create("Rhythm")
rpg = Genre.create("RPG")
puzzle = Genre.create("Puzzle")

xbox = Platform.create("Xbox")
nintendo = Platform.create("Nintendo")
playstation = Platform.create("Playstation")

g1 = Game.create("DarkTide", rpg, xbox)
g2 = Game.create("God of War", rpg, playstation)
    # g3 = Game.create("GoldenEye 007", shooter, nintendo)
    # g4 = Game.create("Super Smash Bros", fighter, nintendo)
    # g5 = Game.create("Legend of Zelda", rpg, nintendo)
    # g6 = Game.create("Super Mario 64", rpg, nintendo)
    # g7 = Game.create("Split-Gate", shooter, xbox)
    # g8 = Game.create("Tekken", fighter, playstation)
    # g9 = Game.create("SSX Tricky", action, playstation)
    # g10 = Game.create("1080", action, nintendo)
    # g11 = Game.create("Wave Racer", race, nintendo)
    # g12 = Game.create("Forza", race, xbox)
    # g13 = Game.create("Gran Tourismo", race, playstation)
    # g14 = Game.create("Halo", shooter, xbox)
    # g15 = Game.create("Contra", shooter, xbox)
    # g16 = Game.create("Call of Duty", shooter, playstation)
    # g17 = Game.create("Skyrim", rpg, playstation)
    # g18 = Game.create("Mega Man", platform, nintendo)
    # g19 = Game.create("Metroid", platform, nintendo)
    # g20 = Game.create("Tetris", platform, nintendo)
    # g21 = Game.create("Left 4 Dead", shooter, xbox)
    # g22 = Game.create("Risk of Rain 2", action, playstation) 
    # g23 = Game.create("Monster Hunter World", rpg, xbox)
    # g24 = Game.create("Rocket League", action, xbox)
    # g25 = Game.create("Elden Ring", rpg, xbox) 
    # g26 = Game.create("CyberPunk2077", rpg, playstation)
    # g27 = Game.create("Onimusha", rpg, playstation)
    # g28 = Game.create("Mortal Kombat", fighter, playstation)
    # g29 = Game.create("Crysis", shooter, playstation)
    # g30 = Game.create("Portal", puzzle, playstation)
    # g31 = Game.create("Grand Theft Auto", action, xbox)
    # g32 = Game.create("Spider-Man", action, playstation)
    # g33 = Game.create("Twisted Metal", action, playstation)
    # g34 = Game.create("Amped", action, xbox)
    # g35 = Game.create("Minecraft", platform, xbox)
    # g36 = Game.create("The Last of Us", rpg, playstation)
    # g37 = Game.create("Resident Evil", action, xbox)
    # g38 = Game.create("Street Fighter II", fighter, nintendo)
    # g39 = Game.create("Assassin's Creed", rpg, playstation)
    # g40 = Game.create("Tony Hawk Pro Skater", action, playstation)
    # g41 = Game.create("Mario Kart", race, nintendo)
    # g42 = Game.create("Donkey Kong", platform, nintendo)
    # g43 = Game.create("Alter Echo", rpg, playstation)
    # g44 = Game.create("eXcite Bike", race, nintendo)
    # g45 = Game.create("Spyro", action, playstation)
    # g46 = Game.create("Sonic", action, nintendo)
    # g47 = Game.create("Apex Legends", shooter, xbox)
    # g48 = Game.create("Final Fantasy", rpg, playstation)
    # g49 = Game.create("DOOM 64", shooter, nintendo)
    # g50 = Game.create("Castlevania symphony of the night", action, nintendo)



