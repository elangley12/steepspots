"""Server for SteepSpots app."""

from flask import Flask, render_template, request, flash, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route("/registration", methods=["POST"])
def register_user():
    """Create a new user."""
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.find_user_by_email(email)

    if user:
        flash("Account already exists. Please try again.")
    else:
        user = crud.create_user(fname, lname, email, password)
        
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def login_user():
    """Login created user."""

    # request email and password from form
    email = request.form.get("email")
    print(f'This is the email {email}')

    password = request.form.get("password")
    print(f'This is the password {password}')

    hashed_pass = generate_password_hash(password, method='sha256', salt_length=10)
    print(f'This is the hashed pass {hashed_pass}')

    # find_user_by_email()
    user = crud.find_user_by_email(email)
    print(f'This is the user {user}')

    # if they exist, check password
    if user:
    #    if hashed_pass == user.password:
        if check_password_hash(user.password, password):
           # login by adding to session
           # redirect to user profile
            session["user"] = user.email
            flash("Login successful!")
            return redirect("/user_profile")

        else:
           # if wrong, flash message to try again
           flash("Wrong email and/or password. Please try again.")
    else:
        # if not, flash message saying create account
        flash("No account found. Please make a new account.")

    # redirect to registration/homepage
    return redirect("/")


@app.route("/logout")
def logout_user():
    """Logout a user."""

    # use pop method to remove key from session
    session.pop("user", None)

    # Flash success message
    flash("Logout successful.")

    return redirect("/")


@app.route("/user_profile")
def show_user_profile():
    """Render user's profile."""

    return render_template("userprofile.html")




if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)