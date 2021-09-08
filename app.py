import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
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

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You have successfully signed up!")
        return redirect(url_for("profile", username=session["user"]))

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
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                flash("Invalid username/password, try again!")
                return redirect(url_for('log_in'))

        else:
            flash("Invalid username/password, try again!")
            return redirect(url_for("log_in"))

    return render_template("pages/authentication.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's profile details from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    profile = mongo.db.users.find_one(
        {"username": session["user"]})
    reviews = list(mongo.db.reviews.find({"user_id": session["user"]}))

    if session["user"]:
        return render_template("/pages/profile.html",
                               username=username,
                               profile=profile,
                               reviews=reviews)

    return redirect(url_for("log_in"))


# edit user profile
@app.route("/edit-profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if session:
        profile_to_edit = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

        # if the user matches the profile to edit
        if profile_to_edit == user["username"]:
            if request.method == "POST":
                update_profile = {
                    "username": request.form.get("username").lower(),
                    "password": generate_password_hash(
                        request.form.get("password")),
                    "bio": request.form.get("bio"),
                    "profile_pic": request.form.get("profile-pic")
                }
                session["user"] = request.form.get("username").lower()
                mongo.db.users.update(
                    {"_id": ObjectId(user_id)}, update_profile)
                flash("You have successfully updated you profile!")
                return redirect(url_for("profile",
                                        username=session['user']))
        else:
            flash("You do not have the permission to update this profile!")
            return redirect(url_for("profile",
                                    username=session["user"]))

    else:
        return redirect(url_for("home_page"))

    return render_template("pages/edit_profile.html", user=user)


# delete profile
@app.route("/delete-profile/<user_id>")
def delete_profile(user_id):
    if session:
        profile_to_delete = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        # if the user matches the profile to edit
        if profile_to_delete == user["username"]:
            mongo.db.reviews.delete_many({"user_id": session["user"]})
            mongo.db.users.delete_one({"_id": ObjectId(user_id)})
            session.pop("user")
            return redirect(url_for("home_page"))
        else:
            flash("You cannot delete this profile!")
            return redirect(url_for("profile",
                                    username=session["user"]))
    else:
        redirect(url_for("home_page"))


@app.route("/log-out")
def log_out():
    # remove user from session cookies
    flash("You have logged out successfully")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/reviews")
def reviews():
    # Get all reviews created & display
    if session:
        reviews = list(mongo.db.reviews.find())
        return render_template("pages/reviews.html", reviews=reviews)
    else:
        return redirect(url_for("home_page"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if session:
        search = request.form.get("search")
        reviews = list(mongo.db.reviews.find(
            {"$text": {"$search": search}}))
        return render_template("pages/reviews.html", reviews=reviews)
    else:
        return redirect(url_for("home_page"))


@app.route("/add-review", methods=["GET", "POST"])
def add_review():

    makes = mongo.db.makes.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    stars = mongo.db.stars.find()

    if session:
        if request.method == "POST":
            review = {
                "boots_name": request.form.get("name"),
                "make": request.form.get("make_id"),
                "image_url": request.form.get("image_url"),
                "category": request.form.get("category"),
                "review_date": datetime.date.today().strftime('%d/%m/%y'),
                "star_rating_id": request.form.get("star_rating_id"),
                "review": request.form.get("review"),
                "user_id": session["user"]
            }

            mongo.db.reviews.insert_one(review)
            flash("Review successfully added!")
            return redirect(url_for("reviews"))

        return render_template("pages/add_review.html",
                               makes=makes,
                               categories=categories,
                               stars=stars,
                               add=True)


# edit boots review
@app.route("/edit-review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    makes = mongo.db.makes.find()
    stars = mongo.db.stars.find()
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session:
        if request.method == "POST":
            update = {
                "boots_name": request.form.get("name"),
                "make": request.form.get("make_id"),
                "image_url": request.form.get("image_url"),
                "category": request.form.get("category"),
                "review_date": request.form.get("review_date"),
                "star_rating_id": request.form.get("star_rating_id"),
                "review": request.form.get("review"),
                "user_id": session["user"]
            }

            mongo.db.reviews.update({"_id": ObjectId(review_id)}, update)
            flash("Review successfully updated!")
            return redirect(url_for("profile", username=username))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("pages/add_review.html",
                               review=review,
                               categories=categories,
                               makes=makes,
                               stars=stars)


# delete boots review
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    # find user to redirect user to profile
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # If the user is logged in
    if session:
        mongo.db.reviews.remove({"_id": ObjectId(review_id)})
        flash("You have successfully deleted your review!")
        return redirect(url_for("profile", username=username))
    # if the user is not logged in
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("reviews"))


@app.route("/manage")
def manage():
    # make sure that the user in session is "admin"
    if session.get("user") == "admin":
        categories = list(mongo.db.categories.find().sort(
            "category_name", 1))
        makes = list(mongo.db.makes.find().sort("name", 1))
        return render_template("pages/manage.html",
                               categories=categories,
                               makes=makes)
    # if the user in session is not "admin"
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # make sure that the user in session is "admin"
    if session.get("user") == "admin":
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            # retrieve the name of the users entry
            category_name = category["category_name"]
            # match the user's entry to a record in the db
            existing_category = mongo.db.categories.find_one(
                {"category_name": category_name})
            # check if it does not exist
            if not existing_category:
                mongo.db.categories.insert_one(category)
                flash("You have successfully added a new category")
                return redirect(url_for("manage"))
            # if it does exist
            else:
                flash("This category already exists, try again!")
                return redirect(url_for("add_category"))

        else:
            return render_template("pages/add_category.html")

    # if the user in session is not "admin"
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if session.get("user") == "admin":
        if request.method == "POST":
            update_category = {
                "category_name": request.form.get("category_name")
            }
            # retrieve the name of the users entry
            update_category_name = update_category["category_name"]
            # match the user's entry to a record in the db
            existing_category = mongo.db.categories.find(
                {"category_name": update_category_name})
            # check if it does not exist
            if not existing_category:
                # update the db with the new category details
                mongo.db.categories.update(
                    {"_id": ObjectId(category_id)}, update_category)
                flash("You have successfully update the category!")
                return redirect(url_for("manage"))
            # if it does exist already
            else:
                flash("This category already exists, try again!")
                return redirect(url_for("add_category"))
        # if method = "GET"
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("pages/edit_category.html", category=category)
    # if session user is not "admin"
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    if session.get("user") == "admin":
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("You have successfully deleted the category!")
        return redirect(url_for("manage"))
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


@app.route("/add_make", methods=["GET", "POST"])
def add_make():
    # make sure that the user in session is "admin"
    if session.get("user") == "admin":
        if request.method == "POST":
            make = {
                "name": request.form.get("name")
            }
            # retrieve the name of the users entry
            make_name = make["name"]
            # match the user's entry to a record in the db
            existing_make = mongo.db.makes.find_one({"name": make_name})
            # check if it does not exist
            if not existing_make:
                mongo.db.makes.insert_one(make)
                flash("You have successfully added a new make")
                return redirect(url_for("manage"))
            # if it does already exist
            else:
                flash("This make already exists, try again!")
                return redirect(url_for("add_make"))
        # if method = "GET"
        return render_template("pages/add_make.html")
    # if the user in session is not "admin"
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


@app.route("/edit_make/<make_id>", methods=["GET", "POST"])
def edit_make(make_id):
    if session.get("user") == "admin":
        if request.method == "POST":
            update_make = {
                "name": request.form.get("name")
            }
            # retrieve the name of the users entry
            update_make_name = update_make["name"]
            # match the user's entry to a record in the db
            existing_make = mongo.db.makes.find(
                {"make": update_make_name})
            if not existing_make:
                # update the db with the new category details
                mongo.db.makes.update(
                    {"_id": ObjectId(make_id)}, update_make)
                flash("You have successfully update the make!")
                return redirect(url_for("manage"))
            else:
                flash("This make already exists, try again!")
                return redirect(url_for("add_make"))
        # if method = "GET"
        else:
            make = mongo.db.makes.find_one({"_id": ObjectId(make_id)})
            return render_template("pages/edit_make.html", make=make)
    # if session user is not "admin"
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


@app.route("/delete_make/<make_id>")
def delete_make(make_id):
    if session.get("user") == "admin":
        mongo.db.makes.remove({"_id": ObjectId(make_id)})
        flash("You have successfully deleted the make!")
        return redirect(url_for("manage"))
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
