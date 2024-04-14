"""Data Models for SteepSpots app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, timedelta

db = SQLAlchemy()

# link to data model:
# https://dbdiagram.io/d/SteepSpots-660c79fb03593b6b6101cfe5


##############################################################################
# MVP table section

class Users(db.Model):
    """Data model for a user."""

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
    ratings = db.relationship('Ratings', back_populates='user')
    reviews = db.relationship('Reviews', back_populates='user')
    tried_stores = db.relationship('AssocUserStores', back_populates='users')
    tea_images = db.relationship('TeaImages', back_populates='user')

    def __repr__(self):
        """Show information on User."""
        return f'<User user_id={self.user_id} email={self.email}>'
    

class Favorites(db.Model):
    """Data model for a user's favorite teas."""

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
    date_favorited = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    user = db.relationship('Users', back_populates='favorites')
    tea = db.relationship('Teas', back_populates='saved_by')

    def __repr__(self):
        """Show info about favorite teas."""

        return f"<Favorites user_id= {self.user_id} tea_id= {self.tea_id}>"


class Ratings(db.Model):
    """Data model for a user's ratings of teas."""

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
    date_rated = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    user = db.relationship('Users', back_populates='ratings')
    tea = db.relationship('Teas', back_populates='ratings')
    reviews = db.relationship('Reviews', uselist=False, back_populates='ratings')

    def __repr__(self):
        """Show info about user tea ratings."""

        return f"<Ratings user_id= {self.user_id} tea_id= {self.tea_id} rating= {self.rating}>"


class Reviews(db.Model):
    """Data model for a user's reviews of teas."""

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
    date_reviewed = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    user = db.relationship('Users', back_populates='reviews')
    tea = db.relationship('Teas', back_populates='reviews')
    ratings = db.relationship('Ratings', uselist=False, back_populates='reviews')

    def __repr__(self):
        """Show info about a user's tea reviews."""

        return f"<Reviews user_id= {self.user_id} tea_id= {self.tea_id} review= {self.review}>"


class Teas(db.Model):
    """Data model for teas tried by users."""

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
    date_added = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    # user = db.relationship() association is found through UserFavorites()
    stores = db.relationship('AssocTeaStores', back_populates='teas')
    sources = db.relationship('AssocTeaSources', back_populates='teas')
    flavors = db.relationship('AssocTeaFlavors', back_populates='teas')
    add_ins = db.relationship('AssocTeaAddIns', back_populates='teas')
    ingredients = db.relationship('AssocTeaIngredients', back_populates='teas')
    food_pairings = db.relationship('AssocTeaPairings', back_populates='teas')
    saved_by = db.relationship('Favorites', back_populates='tea')
    tea_images = db.relationship('TeaImages', back_populates='tea')
    ratings = db.relationship('Ratings', back_populates='tea')
    reviews = db.relationship('Reviews', back_populates='tea')

    def __repr__(self):
        """Show info about teas."""

        return f"<Teas tea_id= {self.tea_id} tea_name= {self.tea_name}>"


class FlavorProfiles(db.Model):
    """Data model for a tea flavor profile."""

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

    teas = db.relationship('AssocTeaFlavors', back_populates='flavors')

    def __repr__(self):
        """Show info about tea flavor profile."""

        return f"<FlavorProfiles flavor_id= {self.flavor_id} tea_flavor= {self.tea_flavor}>"


class TeaAddIns(db.Model):
    """Data model for tea add-ins, i.e. things that are in the cup not the bag."""

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

    teas = db.relationship('AssocTeaAddIns', back_populates='add_ins')

    def __repr__(self):
        """Show info about tea add-ins."""

        return f"<TeaAddIns add_in_id= {self.add_in_id} add_in_name= {self.add_in_name}>"


class TeaIngredients(db.Model):
    """Data model for tea ingredients, i.e. what's in the bag."""

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

    teas = db.relationship('AssocTeaIngredients', back_populates='ingredients')

    def __repr__(self):
        """Show info about tea bag/blend ingredients."""

        return f"<TeaIngredients ingredient_id= {self.ingre_id} ingredient_name= {self.ingre_name}>"


class FoodPairings(db.Model):
    """Data model for foods that pair well with certain teas."""

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

    teas = db.relationship('AssocTeaPairings', back_populates='food_pairings')

    def __repr__(self):
        """Show info about food pairings."""

        return f"<FoodPairings pairing_id= {self.pairing_id} pairing_name= {self.pairing_name}>"


class AssocTeaFlavors(db.Model):
    """Association model between teas and flavors."""

    __tablename__ = 'assocTeaFlavors'

    tea_flavor_id = db.Column(
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
    flavor_id = db.Column(
        db.Integer,
        db.ForeignKey('flavorProfiles.flavor_id'),
        nullable=False
    )

    teas = db.relationship('Teas', back_populates='flavors')
    flavors = db.relationship('FlavorProfiles', back_populates='teas')

    def __repr__(self):
        """Show info about tea_id and flavor_id."""

        return f"<AssocTeaFlavors tea_flavor_id= {self.tea_flavor_id} tea_id= {self.tea_id} flavor_id= {self.flavor_id}>"


class AssocTeaAddIns(db.Model):
    """Association model between teas and add-ins."""

    __tablename__ = 'assocTeaAddIns'

    tea_add_in_id = db.Column(
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
    add_in_id = db.Column(
        db.Integer,
        db.ForeignKey('teaAddIns.add_in_id'),
        nullable=False
    )

    teas = db.relationship('Teas', back_populates='add_ins')
    add_ins = db.relationship('TeaAddIns', back_populates='teas')

    def __repr__(self):
        """Show info about tea_id and add_in_id."""

        return f"<AssocTeaAddIns tea_add_in_id= {self.tea_add_in_id} tea_id= {self.tea_id} add_in_id= {self.add_in_id}>"


class AssocTeaIngredients(db.Model):
    """Association model between teas and ingredients."""

    __tablename__ = 'assocTeaIngredients'

    tea_ingre_id = db.Column(
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
    ingre_id = db.Column(
        db.Integer,
        db.ForeignKey('teaIngredients.ingre_id'),
        nullable=False
    )

    teas = db.relationship('Teas', back_populates='ingredients')
    ingredients = db.relationship('TeaIngredients', back_populates='teas')

    def __repr__(self):
        """Show info about tea_id nad ingre_id."""

        return f"<AssocTeaIngredients tea_ingre_id= {self.tea_ingre_id} tea_id= {self.tea_id} ingre_id= {self.ingre_id}>"


class AssocTeaPairings(db.Model):
    """Association model between teas and food parings."""

    __tablename__ = 'assocTeaPairings'

    tea_pairing_id = db.Column(
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
    pairing_id = db.Column(
        db.Integer,
        db.ForeignKey('foodPairings.pairing_id'),
        nullable=False
    )

    teas = db.relationship('Teas', back_populates='food_pairings')
    food_pairings = db.relationship('FoodPairings', back_populates='teas')

    def __repr__(self):
        """Show info about tea_id and pairing_id."""

        return f"<AssocTeaPairings tea_pairing_id= {self.tea_pairing_id} tea_id= {self.tea_id} pairing_id= {self.pairing_id}>"


##############################################################################
# 2.0+ version table section

class TeaStores(db.Model):
    """Data model for tea stores."""

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

    users = db.relationship('AssocUserStores', back_populates='stores')
    teas = db.relationship('AssocTeaStores', back_populates='stores')

    def __repr__(self):
        """Show info about tea stores, cafes, and retailers."""

        return f"<TeaStores store_id= {self.store_id} tea_id= {self.tea_id} user_id= {self.user_id}>"


class TeaSources(db.Model):
    """Data model for tea sources."""

    __tablename__ = 'teaSources'

    source_id = db.Column(
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

    teas = db.relationship('AssocTeaSources', back_populates='sources')

    def __repr__(self):
        """Show info about tea source locations around the world."""

        return f"<TeaSources source_id= {self.source_id} tea_id= {self.tea_id}>"


class TeaImages(db.Model):
    """Data model for tea images."""

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
    # TODO - correct image class for SQLAlchemy:
    # tea_image = db.Column(
    #     db.Image,
    #     nullable=False
    # )
    date_added = db.Column(
        db.DateTime,
        default=datetime.now()
    )

    user = db.relationship('Users', back_populates='tea_images')
    tea = db.relationship('Teas', back_populates='tea_images')

    def __repr__(self):
        """Show info about tea images."""

        return f"<TeaImages image_id= {self.image_id} tea_id= {self.tea_id} user_id= {self.user_id}>"


class AssocUserStores(db.Model):
    """Association model between users and stores."""

    __tablename__ = 'assocUserStores'

    user_store_id = db.Column(
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
    store_id = db.Column(
        db.Integer,
        db.ForeignKey('teaStores.store_id'),
        nullable=False
    )

    users = db.relationship('Users', back_populates='tried_stores')
    stores = db.relationship('TeaStores', back_populates='users')

    def __repr__(self):
        """Show info about user_id and store_id."""

        return f"<AssocUserStores user_store_id= {self.user_store_id} user_id= {self.user_id} store_id= {self.store_id}>"


class AssocTeaStores(db.Model):
    """Association model between teas and stores."""

    __tablename__ = 'assocTeaStores'

    tea_store_id = db.Column(
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
    store_id = db.Column(
        db.Integer,
        db.ForeignKey('teaStores.store_id'),
        nullable=False
    )

    teas = db.relationship('Teas', back_populates='stores')
    stores = db.relationship ('TeaStores', back_populates='teas')

    def __repr__(self):
        """Show info about tea_id and store_id."""

        return f"<AssocTeaStores tea_store_id= {self.tea_store_id} tea_id= {self.tea_id} store_id= {self.store_id}>"


class AssocTeaSources(db.Model):
    """Association model between teas and sources."""

    __tablename__ = 'assocTeaSources'

    tea_source_id = db.Column(
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
    source_id = db.Column(
        db.Integer,
        db.ForeignKey('teaSources.source_id'),
        nullable=False
    )

    teas = db.relationship('Teas', back_populates='sources')
    sources = db.relationship ('TeaSources', back_populates='teas')

    def __repr__(self):
        """Show info about tea_id and source_id."""

        return f"<AssocTeaSources tea_source_id= {self.tea_source_id} tea_id= {self.tea_id} source_id= {self.source_id}>"



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