"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb steepspots')
os.system('createdb steepspots')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/users.json') as f:
    user_data = json.loads(f.read())