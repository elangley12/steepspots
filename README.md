<img src="https://github.com/elangley12/steepspots/blob/main/static/images/steepspotsintroslide.png?raw=true">
<br/><br/><br/>

### Welcome
Come steep your senses in a global, tea-venturous experience! SteepSpots is a full-stack Flask web app that lets users embark on a flavorful journey around the world. Users can search for new teas by tea origin, create a secure account, and spot teas to curate their favorites list.

Looking ahead, SteepSpots will incorporate Google OAuth for seamless login, leverage open source AI models to offer personalized recommendations, and integrate data visualization libraries for deeper exploration through interactive maps and charts. Stay tuned!

:computer: [VIEW DEMO ON YOUTUBE](https://www.youtube.com/watch?v=rNd63vCU_ls) :computer:

<iframe width="560" height="315" src="https://www.youtube.com/embed/rNd63vCU_ls?si=EIn-XYTsU4hfQFwL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<br/><br/><br/>

## Table of Contents🐛

* [Getting Started](#getting-started)
* [App Features](#app-features)
* [General Info](#gen-info)
<br/><br/><br/>


### <a name="getting-started"></a>Getting Started

These instructions will get you a copy of the project up and running on your local machine for further development, exploration and testing.

#### Prerequisites

Before you begin, be sure to install all requirements within a virtual environment. To learn more about Python's virtualenv tool, [read the documentation](https://virtualenv.pypa.io/en/stable/).

Initiate a virtualenv:

```sh
$ virtualenv env
```

Source the virtualenv:

```sh
$ source env/bin/activate
```

Install requirements:

```sh
(env)$ pip3 install -r requirements.txt
```

Create a PostgreSQL database named `steepspots`, build the model, and seed the data:

```sh
(env)$ createdb steepspots
(env)$ python3 model.py
(env)$ python3 seed_database.py
```

Then, run the application with ```python3 server.py```:

```sh
(env)$ python3 server.py
 * ...
 * Running on http://10.0.0.84:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Connected to the db!
```
You should see similar success messages in the console. If you have any issues getting up and running, please contact the author via GitHub.
<br/><br/><br/>

### <a name="app-features"></a>App Features
Once it is up and running on your local machine, continue to run the demo freely, paying particular attention to the below pages.

#### Home
From the homepage, users have the option to login or create a new SteepSpots account.  

![Nav to Login](https://github.com/elangley12/steepspots/blob/main/static/gifs/nav-to-login.gif?raw=true)
<br/><br/><br/>

On the homepage navbar, users can search for teas based on origin and then see the results without needing to refresh the page. Users who are logged in can "spot" a tea to add it to their Profile page for later exploration.

![Homepage Search](/steepspots/static/gifs/homepage-search.gif)
<br/><br/><br/>

#### Profile
From the user’s profile, users can view their favorited teas, and they can click "unspot" to remove a tea from their favorite’s list. Users can enjoy the dynamically generated carousel from their Profile displaying teas they have favorited, and if a user chooses to unspot a tea from their profile, the carousel will update automatically to match their new list of favorites.

![User Profile](/steepspots/static/gifs/user-profile.gif)
<br/><br/><br/>

### <a name="gen-info"></a>General Information

#### Tech Stack

* [Python3](https://www.python.org/downloads/)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5) and [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
* [PostgresSQL](https://www.postgresql.org/)
* [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
* [AJAX/JSON](https://developer.mozilla.org/en-US/docs/Glossary/AJAX)
* [Bootstrap](https://getbootstrap.com/)
* [Boonaki Tea API](https://boonaki.me/tea-api)

#### Author

Emily Langley

##### Future Development

1.  Google OAuth login
2.  Increased number of teas available in database
3.  Tea rating feature from the user profile
4.  AI agent for Q&A and recommendations
5.  Data visuals for tea profiles

##### Deployment

This application has not been deployed at this time.

##### Permissions

Contact the author for permissions.

##### Acknowledgments

* Ray Traina
* Trew Boisvert
* Hackbright Academy

<img src="/steepspots/static/images/steepspotsthankyou.png">