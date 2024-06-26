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
    # flavor_profiles = crud.show_tea_flavor_profiles()
    # TODO - remove duplicates from crud query
    tea_origins = crud.show_all_tea_origins()

    # to display all results before user selection: query model for all teas, pass to jinja
    all_teas = crud.show_all_teas()
    # print(f"THIS IS all_teas:        {all_teas}")

    return render_template('homepage.html', all_origins=tea_origins, all_teas=all_teas)
    # The all_flavors variable is what will get referenced by Jinja when 
    # displaying flavor profiles in the search drop down


@app.route("/create-account")
def render_registration():
    """Render Create Account page."""

    return render_template('userregistration.html')


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


@app.route("/sign-in")
def render_login():
    """Render Log In page."""

    return render_template('sign-in.html')


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
            session["user"] = user.user_id
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

    user_id = session['user']
    user = crud.find_user_by_id(user_id)
    user_favorites = user.favorites
    # [<Favorite>, <Favorite>]
    # favorite.tea => <Tea> => caffeine, tea_group
    # favorite.user => <User>.favorites


    # print(user_favorites)

    return render_template("userprofile.html", user_favorites=user_favorites)


@app.route('/tea-results.json', methods=["POST"])
def show_tea_results():
    """Return JSON for tea results."""

    # flavor_name = request.json.get('tea_flavor')   
    # TODO - update for origin
    
    # line 139 said another way:
    # request.json dictionary => get key from that dictionary
    # request.json['teaOrigin']
    
    origin = request.json.get('teaOrigin')
    # flavor_instance = crud.find_flavor_by_flavor_name(flavor_name)
    # TODO - call the new crud function
    teas_by_origin = crud.find_teas_by_origin(origin)
    

    results = []
    # TODO - update the response
    for tea in teas_by_origin:
        tea_dictionary = {
            "tea_id": tea.tea_id,
            "tea_group": tea.tea_group,
            "tea_name": tea.tea_name,
            "caff_range_mg": tea.caff_range_mg,
            "tea_img": tea.tea_img,
            "tea_origin": tea.tea_origin,
            "caff_level": tea.caff_level,
            "tea_info": tea.tea_info,
            "tea_color": tea.tea_color,
            "tea_flavor_notes": tea.tea_flavor_notes
        }

        results.append(tea_dictionary)

    
    return jsonify(results)


@app.route('/tea-profile/<tea_id>')
def add_favorite_tea(tea_id):
    """Add tea to user profile."""

    if 'user' in session:
        user_id = session["user"]
        favorite_tea = crud.create_favorite_tea(user_id, tea_id)
        return redirect("/user_profile")
    else:
        flash("Please login or create an account to favorite teas.")
        return redirect('/')





@app.route('/tea-removal/<tea_id>')
def delete_favorite_tea(tea_id):
    """Delete tea from user profile."""

    # grab user_id from session
    user_id = session["user"]

    # call crud.remove_favorite_tea() => get tea_id from userprofile.html 
    remove_favorite_tea = crud.remove_favorite_tea(user_id, tea_id)

    

    # redirect to user profile
    return redirect("/user_profile")









if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)