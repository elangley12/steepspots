"""Server for SteepSpots app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
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

    # SqlAlchemy Query our db for Tea Flavor Profiles
    flavor_profiles = crud.show_tea_flavor_profiles()

    return render_template('homepage.html', all_flavors=flavor_profiles)
    # The all_flavors variable is what will get referenced by Jinja when 
    # displaying flavor profiles in the search drop down


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
    password = request.form.get("password")
    hashed_pass = generate_password_hash(password, method='sha256', salt_length=10)

    # find_user_by_email()
    user = crud.find_user_by_email(email)

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


@app.route('/tea-results.json', methods=["POST"])
def show_tea_results():
    """Return JSON for tea results."""

    flavor_name = request.json.get('tea_flavor')    
    flavor_instance = crud.find_flavor_by_flavor_name(flavor_name)
    

    results = []
    for tea in flavor_instance.teas:
        tea_dictionary = {
            "tea_group": tea.tea_group,
            "tea_brand": tea.tea_brand,
            "brand_flavor": tea.brand_flavor,
            "tea_name": tea.tea_name,
            "tea_class": tea.tea_class,
            "caff_range_mg": tea.caff_range_mg
        }

        results.append(tea_dictionary)

    
    return jsonify(results)


# route to receive flavor selection from js
    # run crud to get all teas from db with selected flavor profile (list of objects)
    # set result list
    # (what results to show on results page?) for loop through each list of objects
        # tea1 > name, brandname > add to results list
        # return result (list of key value pairs that I care about)
    
    
    # (js) for each tea result, make an html element and add to div


# plan B: if ajax is not working, consider jinja templating instead (new page)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)