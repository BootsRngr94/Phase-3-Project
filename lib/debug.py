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
pc = Platform.create("PC")

playstation_pc = Platform.create("Playstation, PC")

nintendo_playstation_pc = Platform.create("Nintendo, Playstation, PC")
nintendo_playstation = Platform.create("Nintendo, Playstation")

xbox_pc = Platform.create("Xbox, PC")
xbox_playstation = Platform.create("Xbox, Playstation")
xbox_playstation_pc = Platform.create("Xbox, Playstation, PC")
xbox_nintendo_playstation = Platform.create("Xbox, Nintendo, Playstation")
xbox_nintendo = Platform.create("Xbox, Nintendo")
all = Platform.create("Xbox, Nintendo, Playstation, PC")


g1 = Game.create("DarkTide", rpg, xbox_pc) 
g2 = Game.create("God of War", rpg, playstation_pc)
g3 = Game.create("GoldenEye 007", shooter, nintendo)
g4 = Game.create("Super Smash Bros", fighter, nintendo)
g5 = Game.create("Legend of Zelda", rpg, nintendo)
g6 = Game.create("Super Mario 64", rpg, nintendo)
g7 = Game.create("Splitgate", shooter, xbox_playstation_pc)
g8 = Game.create("Tekken", fighter, xbox_playstation_pc)
g9 = Game.create("SSX Tricky", action, xbox_playstation_pc)
g10 = Game.create("1080 Snowboarding", action, nintendo)
g11 = Game.create("Wave Race", race, nintendo)
g12 = Game.create("Forza", race, xbox_pc)
g13 = Game.create("Gran Tourismo", race, playstation)
g14 = Game.create("Halo", shooter, xbox_pc)
g15 = Game.create("Contra", shooter, nintendo)
g16 = Game.create("Call of Duty", shooter, all)
g17 = Game.create("Skyrim", rpg, all)
g18 = Game.create("Mega Man", platform, all)   
g19 = Game.create("Metroid", platform, nintendo)
g20 = Game.create("Tetris", platform, all)
g21 = Game.create("Left 4 Dead", shooter, xbox_pc)
g22 = Game.create("Risk of Rain 2", action, playstation) 
g23 = Game.create("Monster Hunter World", rpg, xbox_playstation_pc)
g24 = Game.create("Rocket League", action, all)
g25 = Game.create("Elden Ring", rpg, xbox_playstation_pc) 
g26 = Game.create("CyberPunk2077", rpg, xbox_playstation_pc)
g27 = Game.create("Onimusha", rpg, all)
g28 = Game.create("Mortal Kombat", fighter, all)
g29 = Game.create("Crysis", shooter, all)
g30 = Game.create("Portal", puzzle, all)
g31 = Game.create("Grand Theft Auto", action, xbox_playstation)
g32 = Game.create("Spider-Man", action, playstation_pc)
g33 = Game.create("Twisted Metal", action, playstation_pc)
g34 = Game.create("Amped", action, xbox)
g35 = Game.create("Minecraft", platform, all)
g36 = Game.create("The Last of Us", rpg, playstation_pc)
g37 = Game.create("Resident Evil", action, all)
g38 = Game.create("Street Fighter II", fighter, nintendo)
g39 = Game.create("Assassin's Creed", rpg, xbox_playstation_pc)
g40 = Game.create("Tony Hawk Pro Skater", action, all)
g41 = Game.create("Mario Kart", race, nintendo)
g42 = Game.create("Donkey Kong", platform, nintendo)
g43 = Game.create("Alter Echo", rpg, xbox_playstation)
g44 = Game.create("eXcite Bike", race, nintendo)
g45 = Game.create("Spyro", action, all)
g46 = Game.create("Sonic", action, nintendo)
g47 = Game.create("Apex Legends", shooter, all)
g48 = Game.create("Final Fantasy", rpg, playstation_pc)
g49 = Game.create("DOOM 64", shooter, all)
g50 = Game.create("Castlevania symphony of the night", action, xbox_nintendo_playstation)



