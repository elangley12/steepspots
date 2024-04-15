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
# TODO - add crud functions








################################################################################


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()