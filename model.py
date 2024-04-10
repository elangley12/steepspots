"""Models for SteepSpots app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime
now = datetime.now()

# link to data model:
# https://dbdiagram.io/d/SteepSpots-660c79fb03593b6b6101cfe5


##############################################################################
# Model example


# class Employee(db.Model):
#     """Employee."""

#     __tablename__ = "employees"

#     employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(20), nullable=False, unique=True)
#     state = db.Column(db.String(2), nullable=False, default='CA')
#     dept_code = db.Column(db.String(5), db.ForeignKey('departments.dept_code'))
#     salary = db.Column(db.Integer, nullable=True)

#     dept = db.relationship('Department', back_populates="employees")
#     variable = db.relationship('ClassName', back_populates='other variable name')

#     def __repr__(self):
#         return f"<Employee id={self.employee_id} name={self.name}>"


##############################################################################
#     MVP table section

class Users(db.Model):
    """User."""

    __tablename__ = 'users'

    user_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    fname = db.Column(
        db.String(30),
        nullable=False
    )
    lname = db.Column(
        db.String(30),
        nullable=False
    )
    email = db.Column(
        db.String(75),
        nullable=False,
        unique=True
    )
    password = db.Column(
        db.String(30),
        nullable=False
    )
    start_date = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    favorites = db.relationship('Favorites', back_populates='user')
    # assoc_user_tea = db.relationship('AssocUserTea', back_populates='assocUserTeas')

    def __repr__(self):
        """Show information on User."""
        return f'<User user_id={self.user_id} email={self.email}>'
    

class Favorites(db.Model):
    """User's favorite teas."""

    __tablename__ = 'userFavorites'

    user_fav_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
        nullable=False
    )
    tea_id = db.Column(
        db.Integer,
        db.ForeignKey('teas.tea_id'),
        nullable=False
    )
    # date_favorited = db.Column(db.DateTime, default=`now()`)

    user = db.relationship('Users', back_populates='favorites')
    tea = db.relationship('Teas', back_populates='saved_by')


class Ratings(db.Model):
    """User's ratings of teas."""

    __tablename__ = 'userRatings'

    rating_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
        nullable=False
    )
    tea_id = db.Column(
        db.Integer,
        db.ForeignKey('teas.tea_id'),
        nullable=False
    )
    rating = db.Column( # 1-5 rating
        db.Integer,
        nullable=False
    )
    # date_rated = db.Column(db.DateTime, default=`now()`)

    # tip: in the lecture slides, ratings are users and reviews are employees 
    # in the one-to-one section


class Reviews(db.Model):
    """User's reviews of teas."""

    __tablename__ = 'userReviews'

    review_id = db.Column(
        db.Integer,
        db.ForeignKey('userRatings.rating_id'),
        primary_key=True,
        nullable=False
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
        nullable=False
    )
    tea_id = db.Column(
        db.Integer,
        db.ForeignKey('teas.tea_id'),
        nullable=False
    )
    review = db.Column(
        db.String(255),
        nullable=True
    )
    # date_reviewed = db.Column(db.DateTime, default=`now()`)


class Teas(db.Model):
    """Teas."""

    __tablename__ = 'teas'

    tea_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    tea_group = db.Column( # green, black, oolong, etc
        db.String,
        nullable=False
    )
    tea_brand = db.Column( # lipton, etc
        db.String(75),
        nullable=False
    )
    brand_flavor = db.Column( # none, sleepytime, peace, etc
        db.String(75),
        nullable=False
    )
    tea_name = db.Column( # milk tea with boba, iced tea with lemon
        db.String(50),
        nullable=False
    )
    tea_class = db.Column( # herbal, decaf, caffeinated, etc
        db.String,
        nullable=False
    )
    caff_range_mg = db.Column( # 90-120mg, 0-30 mg, etc
        db.String,
        nullable=False
    )
    hot_cold = db.Column(
        db.String(4),
        nullable=False
    )
    # date_added = db.Column(db.DateTime, default=`now()`)

    saved_by = db.relationship('Favorites', back_populates='tea')


class FlavorProfiles(db.Model):
    """Tea flavor profiles."""

    __tablename__ = 'flavorProfiles'

    flavor_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    tea_flavor = db.Column(
        db.String,
        nullable=False
    )


class TeaAddIns(db.Model):
    """Tea add-ins, i.e. things that are in the cup not the bag."""

    __tablename__ = 'teaAddIns'

    add_in_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    add_in_name = db.Column(
        db.String,
        nullable=False
    )


class TeaIngredients(db.Model):
    """Tea ingredients, i.e. what's in the bag."""

    __tablename__ = 'teaIngredients'

    ingre_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    ingre_name = db.Column(
        db.String,
        nullable=False
    )


class FoodPairings(db.Model):
    """Tea add-ins, i.e. things that are in the cup not the bag."""

    __tablename__ = 'foodPairings'

    pairing_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    pairing_group = db.Column( # cheese, fruit, etc
        db.String,
        nullable=False
    )

    pairing_name = db.Column(
        db.String,
        nullable=False
    )


# class AssocUserTeas(db.Model):
#     """Association table between Users and Teas."""

#     __tablename__ = 'assocUserTeas'

#     user_tea_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     tea_id = db.Column(db.Integer, db.ForeignKey('teas.tea_id'), nullable=False)

#     user = db.relationship('User', back_populates='assocUserTeas')
#     tea = db.relationship('Tea', back_populates='assocUserTeas')

    # this table may be redundant, see userFavorites and decide


class AssocTeaFlavors(db.Model):
    pass


class AssocTeaAddIns(db.Model):
    pass


class AssocTeaIngredients(db.Model):
    pass


class AssocTeaPairings(db.Model):
    pass


##############################################################################
#    2.0+ version table section

class TeaStores(db.Model):
    """Tea stores."""

    __tablename__ = 'teaStores'

    store_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    tea_id = db.Column(
        db.Integer,
        db.ForeignKey('teas.tea_id'),
        nullable=False
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
        nullable=False
    )
    lat_long = db.Column(
        db.Integer,
        nullable=False
    )
    google_maps_loc = db.Column(
        db.Integer,
        nullable=False
    )
    continent = db.Column(
        db.String,
        nullable=False
    )
    country = db.Column(
        db.String,
        nullable=False
    )
    city = db.Column(
        db.String,
        nullable=False
    )
    date_added = db.Column(
        db.DateTime,
        default=datetime.now()
    )


class TeaSources(db.Model):
    pass


class TeaImages(db.Model):
    """Tea images."""

    __tablename__ = 'teaImages'

    image_id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    tea_id = db.Column(
        db.Integer,
        db.ForeignKey('teas.tea_id'),
        nullable=False
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.user_id'),
        nullable=False
    )
    tea_image = db.Column(
        db.Image,
        nullable=False
    )


class AssocUserStores(db.Model):
    pass


class AssocTeaStores(db.Model):
    pass


class AssocTeaSources(db.Model):
    pass



##############################################################################
# Connection to DB

def connect_to_db(flask_app, db_uri="postgresql:///steepspots", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)