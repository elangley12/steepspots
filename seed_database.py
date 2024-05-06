"""Script to seed database."""

import os
import json
import requests
# from random import choice, randint
# from datetime import datetime

import crud
import model
import server

os.system('dropdb steepspots')
os.system('createdb steepspots')

model.connect_to_db(server.app)
model.db.create_all()




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

res = requests.get('https://boonakitea.cyclic.app/api/teas')
api_results = res.json()

teas_in_db = []
for parent_dict in api_results:
    # data type of parent_dict is dictionary
    # when keys not consistent in json, we create an if/else to only add what 
    # teas have types
    if 'types' in parent_dict:
        for tea in parent_dict['types'].keys():
            # make a dictionary for each tea type then append to a master 
            # tea dictionary
            individual_tea_dict = {
                "caff_range_mg": parent_dict['types'][tea]['caffeine'],
                "tea_name": parent_dict['types'][tea]['name'],
                "tea_group": parent_dict['types'][tea]['type'],
                
                # not in model yet
                "tea_img": parent_dict['types'][tea]['image'],
                "tea_origin": parent_dict['types'][tea]['origin'],
                "caff_level": parent_dict['types'][tea]['caffeineLevel'],
                "tea_info": parent_dict['types'][tea]['decription'],
                "tea_color": parent_dict['types'][tea]['colorDescription'],
                "tea_flavor_notes": parent_dict['types'][tea]['tasteDescription'],
                # "web_sources": parent_dict['types'][tea]['sources']  =>  # because this is a list, it would actual be better to make a new table for URLs
            }

            # take this information and pass it to the crud.create_tea()
            db_tea = crud.create_tea(individual_tea_dict)


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

# flavor_bitter = model.FlavorProfiles.query.get(1)
# flavor_earthy = model.FlavorProfiles.query.get(2)
# flavor_floral = model.FlavorProfiles.query.get(3)
# flavor_fruity = model.FlavorProfiles.query.get(4)
# flavor_grassy = model.FlavorProfiles.query.get(5)
# flavor_herbaceous = model.FlavorProfiles.query.get(6)
# flavor_malty = model.FlavorProfiles.query.get(7)
# flavor_mineral = model.FlavorProfiles.query.get(8)
# flavor_nutty = model.FlavorProfiles.query.get(9)
# flavor_oceanic = model.FlavorProfiles.query.get(10)
# flavor_rich = model.FlavorProfiles.query.get(11)
# flavor_smokey = model.FlavorProfiles.query.get(12)
# flavor_smooth = model.FlavorProfiles.query.get(13)
# flavor_spiced = model.FlavorProfiles.query.get(14)
# flavor_sweet = model.FlavorProfiles.query.get(15)
# flavor_umami = model.FlavorProfiles.query.get(16)
# flavor_vegetal = model.FlavorProfiles.query.get(17)

# tea1_green = model.Teas.query.get(1)
# tea1_green.flavors.append(flavor_bitter)
# # model.db.session.commit()
# tea1_green.flavors.append(flavor_grassy)
# # model.db.session.commit()
# tea1_green.flavors.append(flavor_vegetal)
# # model.db.session.commit()

# tea2_mint = model.Teas.query.get(2)
# tea2_mint.flavors.append(flavor_herbaceous)
# tea2_mint.flavors.append(flavor_spiced)
# # model.db.session.commit()

# tea3_chai = model.Teas.query.get(3)
# tea3_chai.flavors.append(flavor_spiced)
# tea3_chai.flavors.append(flavor_bitter)
# tea3_chai.flavors.append(flavor_earthy)
# # model.db.session.commit()

# tea4_tulsi = model.Teas.query.get(4)
# tea4_tulsi.flavors.append(flavor_herbaceous)
# tea4_tulsi.flavors.append(flavor_floral)
# tea4_tulsi.flavors.append(flavor_spiced)
# tea4_tulsi.flavors.append(flavor_sweet)
# tea4_tulsi.flavors.append(flavor_smooth)
# # model.db.session.commit()

# tea5_peace = model.Teas.query.get(5)
# tea5_peace.flavors.append(flavor_herbaceous)
# tea5_peace.flavors.append(flavor_floral)
# tea5_peace.flavors.append(flavor_earthy)
# tea5_peace.flavors.append(flavor_spiced)
# tea5_peace.flavors.append(flavor_sweet)
# tea5_peace.flavors.append(flavor_smokey)
# model.db.session.commit()