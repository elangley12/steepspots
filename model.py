from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

#     def __repr__(self):
#         return f"<Employee id={self.employee_id} name={self.name}>"


##############################################################################
#     MVP table section

class Users(db.model):
    """User."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fname = db.Column(db.Varchar(30), nullable=False)
    lname = db.Column(db.Varchar(30), nullable=False)
    email = db.Column(db.Varchar(75), nullable=False)
    password = db.Column(db.Varchar(30), nullable=False)
    # start_date = db.Column(db.DateTime, default=`now()`)


class UserFavorites(db.model):
    """User's favorite teas."""

    __tablename__ = 'userFavorites'

    user_fav_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    tea_id = db.Column(db.Integer, db.ForeignKey('teas.tea_id'), nullable=False)
    # date_favorited = db.Column(db.DateTime, default=`now()`)


class UserRatings(db.model):
    """User's ratings of teas."""

    __tablename__ = 'userRatings'

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    tea_id = db.Column(db.Integer, db.ForeignKey('teas.tea_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # date_rated = db.Column(db.DateTime, default=`now()`)


class UserReviews(db.model):
    """User's reviews of teas."""

    __tablename__ = 'userReviews'

    review_id = db.Column(db.Integer, db.ForeignKey('userRatings.rating_id'), primary_key=True, autoincrement=True, nullable=False) # am I doing this right if review_id and rating_id are one to one?
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    tea_id = db.Column(db.Integer, db.ForeignKey('teas.tea_id'), nullable=False)
    review = db.Column(db.varchar(255), nullable=True)
    # date_reviewed = db.Column(db.DateTime, default=`now()`)


class Teas(db.model):
    pass


class FlavorProfiles(db.model):
    pass


class TeaAddIns(db.model):
    pass


class TeaIngredients(db.model):
    pass


class FoodPairings(db.model):
    pass


class AssocUserTeas(db.model):
    pass


class AssocTeaFlavors(db.model):
    pass


class AssocTeaAddIns(db.model):
    pass


class AssocTeaIngredients(db.model):
    pass


class AssocTeaPairings(db.model):
    pass


##############################################################################
#    2.0+ version table section

class TeaStores(db.model):
    pass


class TeaSources(db.model):
    pass


class TeaImages(db.model):
    pass


class AssocUserStores(db.model):
    pass


class AssocTeaStores(db.model):
    pass


class AssocTeaSources(db.model):
    pass



##############################################################################
# Connection to DB

def connect_to_db(flask_app, db_uri="postgresql:///your-database-name", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)