import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# home page
@app.route("/")
def home_page():
    """
    takes user to homepage
    """
    return render_template('pages/home.html')


# sign up new user
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    """
    checks if method is post
    if user exists, redirect to sign-up page
    if new user, insert new user to db
    put the new user into session
    """

    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, try again!")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "profile_pic": request.form.get("profile-pic")
        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username").lower()
        flash("You have successfully signed up!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("pages/authentication.html", sign_up=True)


# login to profile
@app.route("/login", methods=["GET", "POST"])
def login():

    """
    check if method is post
    check if user exists, check if pw matches
    put user into session & redirect user to user profile
    if wrong pw, flash message & redirect
    if user does not exist, flash message & redirect
    """

    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"],
               request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                flash("Invalid username/password, try again!")
                return redirect(url_for('login'))

        else:
            flash("Invalid username/password, try again!")
            return redirect(url_for("login"))

    return render_template("pages/authentication.html")


# profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    """
    grab the session user's profile details from db
    grab the user's reviews from db in a list
    redirect user to login page if user not in session
    """

    if session["user"]:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        profile = mongo.db.users.find_one(
            {"username": session["user"]})
        reviews = list(mongo.db.reviews.find({"user_id": session["user"]}))
        return render_template("/pages/profile.html",
                               username=username,
                               profile=profile,
                               reviews=reviews)

    return redirect(url_for("login"))


# edit user profile
@app.route("/edit-profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):

    """
    if user in session grab profile to edit from db
    grab user in session from db based on user id

    if they match each other & if method = post
    grab form input from user & update db
    redirect user to updated profile page
    if the profiles don't match, redirect to profile

    if user not in session, redirect home
    """

    if session:
        profile_to_edit = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

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

    """
    if the user is in session grab profile to edit
    grab the user in session from the db
    if the two users match, delete user's reviews & profile
    remove user from session & redirect to homepage
    if the two users don't match, flash msg & redirect
    """

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


# log out
@app.route("/log-out")
def log_out():

    """
    flash msg and remove user from session
    redirect login
    """

    flash("You have logged out successfully")
    session.pop("user")
    return redirect(url_for("login"))


# reviews page
@app.route("/reviews")
def reviews():

    """
    if user in session grab list of reviews
    render reviews page
    else, render home page
    """

    if session:
        reviews = list(mongo.db.reviews.find())
        return render_template("pages/reviews.html", reviews=reviews)
    else:
        return redirect(url_for("home_page"))


# search boots reviews
@app.route("/search", methods=["GET", "POST"])
def search():

    """
    if user in session grab search input from form
    grab filtered list of reviews from db based on search
    render reviews page
    render homepage if user not in session
    """

    if session:
        search = request.form.get("search")
        reviews = list(mongo.db.reviews.find(
            {"$text": {"$search": search}}))
        return render_template("pages/reviews.html", reviews=reviews)
    else:
        return redirect(url_for("home_page"))


# add boots review
@app.route("/add-review", methods=["GET", "POST"])
def add_review():

    """
    if user in session grab makes, categories, stars
    if methods = post grab reviews object insert review in db
    redirect to reviews page
    if method = get render add review page
    """

    if session:
        makes = mongo.db.makes.find().sort("makes", 1)
        categories = mongo.db.categories.find().sort("category_name", 1)
        stars = mongo.db.stars.find()
        if request.method == "POST":
            review = {
                "boots_name": request.form.get("name"),
                "make": request.form.get("make_id"),
                "image_url": request.form.get("image_url"),
                "category": request.form.get("category"),
                "review_date": date.today().strftime('%d/%m/%y'),
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

    """
    check if user is in session grab user's reviews, makes, stars & username
    if method = post grab updated review object
    insert updated review object to db
    flash msg & redirect to profile page
    if method = get grab categories from db and display alphabetically
    render add review page
    """

    if session:
        review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
        makes = mongo.db.makes.find().sort("name", 1)
        stars = mongo.db.stars.find()
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
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

    """
    if user in session find user's username
    find review to delete with review_id
    flash msg & redirect to profile page
    if user not in session, flash msg & redirect to reviews
    """

    if session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        mongo.db.reviews.remove({"_id": ObjectId(review_id)})
        flash("You have successfully deleted your review!")
        return redirect(url_for("profile", username=username))
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


# manage page
@app.route("/manage")
def manage():

    """
    make sure that the user in session is "admin"
    grab categories & makes from db & sort alphabetically
    render manage page
    if user in session, flash msg & redirect home
    """

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


# add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    """
    make sure that the user in session is "admin"
    if method=post grab the new category from db and get it's name
    match it to an existing category & check if it does not exist in db
    if not, insert the new category to db & flash msg & redirect
    if new category alreay exists, flash msg & render add category pg
    if method=get render add category page
    if user not in session flash msg & redirect home
    """

    if session.get("user") == "admin":
        if request.method == "POST":
            category = {
                "category_name": request.form.get("category_name")
            }
            category_name = category["category_name"]
            existing_category = mongo.db.categories.find_one(
                {"category_name": category_name})
            if not existing_category:
                mongo.db.categories.insert_one(category)
                flash("You have successfully added a new category")
                return redirect(url_for("manage"))
            else:
                flash("This category already exists, try again!")
                return redirect(url_for("add_category"))
        else:
            return render_template("pages/add_category.html")
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


# edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    """
    make sure that the user in session is "admin"
    if method=post grab the category to edit from form and get it's name
    match it to an existing category & check if it does not exist in db
    if not, insert the updated category to db & flash msg & redirect
    if it exists flash msg & redirect to edit category
    if method=get get the category to edit & render edit category page
    if session user is not admin redirect home
    """

    if session.get("user") == "admin":
        if request.method == "POST":
            update_category = {
                "category_name": request.form.get("category_name")
            }
            update_category_name = update_category["category_name"]
            existing_category = mongo.db.categories.find(
                {"category_name": update_category_name})
            if not existing_category:
                mongo.db.categories.update(
                    {"_id": ObjectId(category_id)}, update_category)
                flash("You have successfully update the category!")
                return redirect(url_for("manage"))
            else:
                flash("This category already exists, try again!")
                return redirect(url_for("add_category"))
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("pages/edit_category.html", category=category)
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


# delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    """
    if user in session is admin
    find category to remove with category_id and remove from db
    flsh msg & redirect to manage
    if user in session is not admin flash msg & redirect home
    """

    if session.get("user") == "admin":
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("You have successfully deleted the category!")
        return redirect(url_for("manage"))
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


# add make
@app.route("/add_make", methods=["GET", "POST"])
def add_make():

    """
    if user in session is "admin" and method=post
    get new make from form and get it's name
    check if that make exists in db already
    if new make does not already exist in db add new make to db & redirect
    if new make alreay exists, flash msg & redirect to add make
    if method=get render add make page
    if session user is not admin flash msg & redirect home
    """

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


# edit make
@app.route("/edit_make/<make_id>", methods=["GET", "POST"])
def edit_make(make_id):

    """
    if user in session is "admin" and method=post
    get make to edit from make_id and get it's name
    check if that make exists in db already
    if the make does not already exist in db update make to db & redirect
    if the make alreay exists, flash msg & redirect to edit make
    if method=get render edit make page
    if session user is not admin flash msg & redirect home
    """

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
                flash("You have successfully updated the make!")
                return redirect(url_for("manage"))
            else:
                flash("This make already exists, try again!")
                return redirect(url_for("edit_make"))
        # if method = "GET"
        else:
            make = mongo.db.makes.find_one({"_id": ObjectId(make_id)})
            return render_template("pages/edit_make.html", make=make)
    # if session user is not "admin"
    else:
        flash("You cannot perform this action!")
        return redirect(url_for("home_page"))


# delete make
@app.route("/delete_make/<make_id>")
def delete_make(make_id):

    """
    if user in session is admin
    find make to remove with make_id and remove from db
    flsh msg & redirect to manage
    if user in session is not admin flash msg & redirect home
    """

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
