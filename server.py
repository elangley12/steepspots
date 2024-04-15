"""Server for SteepSpots app."""

from flask import Flask, render_template, request, flash, session, redirect

app = Flask(__name__)
#   ... your routes, view functions, and everything else can come later ...






if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)