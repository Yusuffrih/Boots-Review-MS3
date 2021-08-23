import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('pages/home.html')


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, try again!")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "bio": request.form.get("bio"),
            "profile_pic": request.form.get("profile-pic")
        }
        mongo.db.users.insert_one(sign_up)
        return redirect(url_for("profile"))

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully signed up!")

    return render_template("pages/authentication.html", sign_up=True)


@app.route("/log-in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check to see if the password matches that of the db
            if check_password_hash(existing_user["password"],
               request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile"))

            else:
                flash("Invalid username/password, try again!")
                return redirect(url_for('log_in'))

        else:
            flash("Invalid username/password, try again!")
            return redirect(url_for("log_in"))

    return render_template("pages/authentication.html")


@app.route("/profile")
def profile():
    return render_template("/pages/profile.html")


@app.route("/reviews")
def reviews():
    reviews = mongo.db.reviews.find()
    return render_template("pages/reviews.html", reviews=reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
