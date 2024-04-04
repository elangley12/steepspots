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
    pass


class UserFavorites(db.model):
    pass


class UserRatings(db.model):
    pass


class UserReviews(db.model):
    pass


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