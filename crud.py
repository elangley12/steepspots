"""CRUD operations."""

# will need to bring back in tables as features added, see model.py

from model import(
    db,
    Users,
    Favorites,
    Ratings,
    Reviews,
    Teas,
    FlavorProfiles,
    AssocTeaFlavors
    )
from werkzeug.security import generate_password_hash, check_password_hash

################################################################################
#USERS

# MVP
# create_user()
def create_user(fname, lname, email, password):
    """Create and return a new user."""

    new_user = Users(
        fname=fname,
        lname=lname,
        email=email,
        password=generate_password_hash(password, method='sha256', salt_length=10)
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user


# find_user_by_email()
def find_user_by_email(email):
    """Return a user by email."""

    return Users.query.filter(Users.email == email).first()


def find_user_by_id(user_id):
    """Return a user by ID."""

    return Users.query.filter(Users.user_id == user_id).first()


# delete_user()
def delete_user(user_id):
    """Delete a user from the database."""

    user = Users.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return


# TODO - Later version CRUD operations:
# find_user_by_id()
# find_user_by_fname()
# find_user_by_lname()
# find_user_by_date()


################################################################################
#TEAS

# MVP
# create_tea()
def create_tea(tea_dict):
    """Create and return a new tea."""

    new_tea = Teas(
        tea_group = tea_dict['tea_group'],
        tea_name = tea_dict['tea_name'],
        caff_range_mg = tea_dict['caff_range_mg'],
        tea_img = tea_dict['tea_img'],
        tea_origin = tea_dict['tea_origin'],
        caff_level = tea_dict['caff_level'],
        tea_info = tea_dict['tea_info'],
        tea_color = tea_dict['tea_color'],
        tea_flavor_notes = tea_dict['tea_flavor_notes']
    )

    # db.session.add(new_tea)
    # db.session.commit()

    return new_tea


def show_all_teas():
    """Return all teas in model."""

    return Teas.query.all()


def find_tea_by_flavor(flavor):
    """Return a tea by flavor."""
    # Teas.flavors contains flavor?
    return Teas.query.filter(Teas.flavors == flavor).first()
    # tea = Tea(...)
    # tea.flavors => list of flavor records
    #   flavor1 = FlavorProfiles(...)
    #   flavor2 = FlavorProfiles(...)
    # tea.flavors => [<Flavor1>, <Flavor2>]

def find_teas_by_origin(origin):
    """Find a tea by origin."""

    return Teas.query.filter(Teas.tea_origin == origin).all()


def show_all_tea_origins():
    """Return all tea origins."""

    # TODO - update this func so it queries the Teas table and return a list of origins
    # query to get all flavor profiles from database
    # return FlavorProfiles.query.all()

    return db.session.query(Teas.tea_origin).all() # [('China'), ('India')...]

# TODO - Later version CRUD operations:
# delete_tea()
# find_tea_by_id()
# find_tea_by_group()
# find_tea_by_brand()
# find_tea_by_brand_flavor()
# find_tea_by_name()
# find_tea_by_class()
# find_tea_by_caff_level()
# find_tea_by_temp()
# find_tea_by_date()


################################################################################
#FLAVOR PROFILES

def create_flavor_profile(tea_flavor):
    """Create and return flavor profile tags for teas."""

    flavor_options = FlavorProfiles(
        tea_flavor=tea_flavor
    )

    db.session.add(flavor_options)
    db.session.commit()

    return flavor_options


def show_tea_flavor_profiles():
    """Return all tea flavor profiles."""

    # TODO - update this func so it queries the Teas table and return a list of origins
    # query to get all flavor profiles from database
    return FlavorProfiles.query.all()


# new function
    # query to filter teas by selected flavor profile
def find_flavor_by_flavor_name(flavor_name):

    return FlavorProfiles.query.filter_by(tea_flavor=flavor_name).first()


################################################################################
#ASSOC TEA FLAVORS

def associate_tea_to_flavors(tea, flavors):
    """Create and return tea to flavor profile tags."""

    tea_flavor_profile = AssocTeaFlavors(teas=tea, flavors=flavors)

    db.session.add(tea_flavor_profile)
    db.session.commit()

    return tea_flavor_profile


################################################################################
#FAVORITES

# create favorite tea (create row in Favorites())
def create_favorite_tea(user_id, tea_id):
    """Create and return a tea favorited by a user."""

    favorite_tea = Favorites(
        user_id = user_id,
        tea_id = tea_id
    )

    # if I change tea_id to the primary key on Favorites(), how will errors be 
    # handled by SQLAlchemy?
    fav_query_result = Favorites.query.filter_by(user_id=user_id, tea_id=tea_id).count()

    if fav_query_result >= 1:
        print("Already a favorite tea!")
    else:
        print("New tea favorited!")
        db.session.add(favorite_tea)
        db.session.commit()

    return favorite_tea



def remove_favorite_tea(user_id, tea_id):
    """Remove a tea favorited by the user."""

    # need to know what tea_id the user is trying to delete
    # query for that tea_id in Favorites

    tea_to_delete = Favorites.query.filter_by(user_id=user_id, tea_id=tea_id).first()
    print(f"TEA_TO_DELETE is:",tea_to_delete)

    # fav_id = tea_to_delete.user_fav_id
    # print(f"USER_FAV_ID is: {fav_id}")

    # what about deleting by user_fav_id? 
    # I think the duplicates are confusing SQLAlchemy

    db.session.delete(tea_to_delete)
    db.session.commit()

    print(f"*********Tea {tea_id} removed from User {user_id} Favorites()")





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()