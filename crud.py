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
        password=generate_password_hash(password, method='sha256')
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user


# find_user_by_email()
def find_user_by_email(email):
    """Return a user by email."""

    return Users.query.filter(Users.email == email).first()


# delete_user()



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
# delete_tea()

# TODO - Later version CRUD operations:
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



################################################################################
#TEA ADD INS



################################################################################
#TEA INGREDIENTS



################################################################################
#FOOD PAIRINGS



################################################################################
#ASSOC TEA FLAVORS



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