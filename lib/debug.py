#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models import Game

Game.create_table()

ipdb.set_trace()
