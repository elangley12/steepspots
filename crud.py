"""CRUD operations."""

from model import(
    db,
    Users,
    Favorites,
    Ratings,
    Reviews,
    Teas,
    FlavorProfiles,
    TeaAddIns,
    TeaIngredients,
    FoodPairings,
    AssocTeaFlavors,
    AssocTeaAddIns,
    AssocTeaIngredients,
    AssocTeaPairings,
    TeaStores,
    TeaSources,
    TeaImages,
    AssocUserStores,
    AssocTeaStores,
    AssocTeaSources,)
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
#FAVORITES



################################################################################
#RATINGS



################################################################################
#REVIEWS



################################################################################
#TEAS

# MVP
# create_tea()
def create_tea(tea_group, tea_brand, brand_flavor, tea_name, tea_class, caff_range_mg, hot_cold):
    """Create and return a new tea."""

    new_tea = Teas(
        tea_group = tea_group,
        tea_brand = tea_brand,
        brand_flavor = brand_flavor,
        tea_name = tea_name,
        tea_class = tea_class,
        caff_range_mg = caff_range_mg,
        hot_cold = hot_cold
    )

    db.session.add(new_tea)
    db.session.commit()

    return new_tea


# TODO find_tea_by_flavor_profile()

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


################################################################################
#TEA ADD INS



################################################################################
#TEA INGREDIENTS



################################################################################
#FOOD PAIRINGS



################################################################################
#ASSOC TEA FLAVORS

def associate_tea_to_flavors(tea, flavors):
    """Create and return tea to flavor profile tags."""

    tea_flavor_profile = AssocTeaFlavors(teas=tea, flavors=flavors)

    db.session.add(tea_flavor_profile)
    db.session.commit()

    return tea_flavor_profile


################################################################################
#ASSOC TEA ADD INS



################################################################################
#ASSOC TEA INGREDIENTS



################################################################################
#ASSOC TEA PAIRINGS



################################################################################
#TEA STORES



################################################################################
#TEA SOURCES



################################################################################
#TEA IMAGES



################################################################################
#ASSOC USER STORES



################################################################################
#ASSOC TEA STORES



################################################################################
#ASSOC TEA SOURCES








################################################################################


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()