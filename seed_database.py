"""Script to seed database."""

import os
import json
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
    "Bitter",       #1
    "Earthy",       #2
    "Floral",       #3
    "Fruity",       #4
    "Grassy",       #5
    "Herbaceous",   #6
    "Malty",        #7
    "Mineral",      #8
    "Nutty",        #9
    "Oceanic",      #10
    "Rich",         #11
    "Smoky",        #12
    "Smooth",       #13
    "Spiced",       #14
    "Sweet",        #15
    "Umami",        #16
    "Vegetal"       #17
]

for tag in tea_flavor_tags:
    tea_flavor = tag
    flavor_profiles = crud.create_flavor_profile(tea_flavor)


# create test teas

teas_in_db = []
for tea in tea_data:
    tea_group, tea_brand, brand_flavor, tea_name, tea_class, caff_range_mg, hot_cold = (
        tea["tea_group"],
        tea["tea_brand"],
        tea["brand_flavor"],
        tea["tea_name"],
        tea["tea_class"],
        tea["caff_range_mg"],
        tea["hot_cold"]
    )

    db_tea = crud.create_tea(
        tea_group,
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


# tea1= model.Teas.query.get(1)
# flavor1 = model.FlavorProfiles.query.get(1)
# tea1.flavors.append(flavor1)
# model.db.session.commit()

    # grab tea to add flavors to (store each tea in a variable)
    # grab flavors to add to tea (store each flavor in a variable)
    # use tea.flavor.append(<flavor>) to make associations
    # commit everything

flavor_bitter = model.FlavorProfiles.query.get(1)
flavor_earthy = model.FlavorProfiles.query.get(2)
flavor_floral = model.FlavorProfiles.query.get(3)
flavor_fruity = model.FlavorProfiles.query.get(4)
flavor_grassy = model.FlavorProfiles.query.get(5)
flavor_herbaceous = model.FlavorProfiles.query.get(6)
flavor_malty = model.FlavorProfiles.query.get(7)
flavor_mineral = model.FlavorProfiles.query.get(8)
flavor_nutty = model.FlavorProfiles.query.get(9)
flavor_oceanic = model.FlavorProfiles.query.get(10)
flavor_rich = model.FlavorProfiles.query.get(11)
flavor_smokey = model.FlavorProfiles.query.get(12)
flavor_smooth = model.FlavorProfiles.query.get(13)
flavor_spiced = model.FlavorProfiles.query.get(14)
flavor_sweet = model.FlavorProfiles.query.get(15)
flavor_umami = model.FlavorProfiles.query.get(16)
flavor_vegetal = model.FlavorProfiles.query.get(17)

tea1_green = model.Teas.query.get(1)
tea1_green.flavors.append(flavor_bitter)
# model.db.session.commit()
tea1_green.flavors.append(flavor_grassy)
# model.db.session.commit()
tea1_green.flavors.append(flavor_vegetal)
# model.db.session.commit()

tea2_mint = model.Teas.query.get(2)
tea2_mint.flavors.append(flavor_herbaceous)
tea2_mint.flavors.append(flavor_spiced)
# model.db.session.commit()

tea3_chai = model.Teas.query.get(3)
tea3_chai.flavors.append(flavor_spiced)
tea3_chai.flavors.append(flavor_bitter)
tea3_chai.flavors.append(flavor_earthy)
# model.db.session.commit()

tea4_tulsi = model.Teas.query.get(4)
tea4_tulsi.flavors.append(flavor_herbaceous)
tea4_tulsi.flavors.append(flavor_floral)
tea4_tulsi.flavors.append(flavor_spiced)
tea4_tulsi.flavors.append(flavor_sweet)
tea4_tulsi.flavors.append(flavor_smooth)
# model.db.session.commit()

tea5_peace = model.Teas.query.get(5)
tea5_peace.flavors.append(flavor_herbaceous)
tea5_peace.flavors.append(flavor_floral)
tea5_peace.flavors.append(flavor_earthy)
tea5_peace.flavors.append(flavor_spiced)
tea5_peace.flavors.append(flavor_sweet)
tea5_peace.flavors.append(flavor_smokey)
model.db.session.commit()


# TODO - for each tea, attach flavor profile using AssocTeaFlavors() to make connections:
# make a tea and flavor dictionary pulling from teas.json and tea_flavor_tags options above for each tea
# for each tea, add the flavor to crud function and create connection in db for AssocTeaFlavors()

    # test: query checking for profile connections, then make html with search bar (look at ajax lab order melons)