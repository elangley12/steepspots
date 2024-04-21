"""Script to seed database."""

import os
# import json
# from random import choice, randint
# from datetime import datetime

import crud
import model
import server

os.system('dropdb steepspots')
os.system('createdb steepspots')

model.connect_to_db(server.app)
model.db.create_all()


# Load user data from JSON file:
with open('data/teas.json') as f:
    tea_data = json.loads(f.read())



# create test users

for n in range(10):
    fname =f'First{n}'
    lname = f'Last{n}'
    email = f"testuser{n}@test.com"
    password = "test123"

    user = crud.create_user(fname, lname, email, password)



# create tea flavor profiles

tea_flavor_tags = [
    "Bitter",
    "Earthy",
    "Floral",
    "Fruity",
    "Grassy",
    "Herbaceous",
    "Malty",
    "Mineral",
    "Nutty",
    "Oceanic",
    "Rich",
    "Smoky",
    "Smooth",
    "Spiced"
    "Sweet",
    "Umami",
    "Vegetal"
]

for tag in tea_flavor_tags:
    tea_flavor = tag
    flavor_profiles = crud.create_flavor_profile(tea_flavor)


# create test teas

teas_in_db = []
for tea in tea_data:
    tea_brand, brand_flavor, tea_name, tea_class, caff_range_mg, hot_cold = (
        tea["tea_brand"],
        tea["brand_flavor"],
        tea["tea_name"],
        tea["tea_class"],
        tea["caff_range_mg"],
        tea["hot_cold"]
    )

    db_tea = crud.create_tea(
        tea_brand, 
        brand_flavor, 
        tea_name, 
        tea_class, 
        caff_range_mg, 
        hot_cold
    )

    teas_in_db.append(db_tea)

model.db.session.add_all(teas_in_db)
model.db.session.commit()


# TODO - for each tea, attach flavor profile using AssocTeaFlavors() to make connections:
# make a tea and flavor dictionary pulling from teas.json and tea_flavor_tags options above for each tea
# for each tea, add the flavor to crud function and create connection in db for AssocTeaFlavors()

    # test: query checking for profile connections, then make html with search bar (look at ajax lab order melons)