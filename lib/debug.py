#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models import Game
import ipdb

Game.create_table()

ipdb.set_trace()
