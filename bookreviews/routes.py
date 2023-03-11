from flask import (Flask, render_template, session, url_for, redirect,
                   request, flash)
from bookreviews import app, db
from bookreviews.models import Books, Roles, Teachers, Students, Reviews
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("base.html")

# register new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form["email"]
        # first query to check if user already exists
        found_user = Teachers.query.filter_by(email=user).first()
        if found_user:
            flash("User already exists with this email address.")
            return redirect(url_for("register"))
        # if no email matches, register new user by adding to db
        else:
            new_user = Teachers(
                email=request.form.get("email").lower(),
                prefix=request.form.get("prefix").lower(),
                surname=request.form.get("surname").lower(),
                school=request.form.get("school").lower(),
                role=1,
                password=generate_password_hash(request.form.get("password")))

            db.session.add(new_user)
            db.session.commit()

        # put the new user into 'session' cookie
            session["new_user"] = request.form.get("email").lower()
            flash("Registration Successful")
            return redirect(url_for("home"))
    # NEED TO RETURN TO THIS SECTION TO ROUTE BACK TO ACCOUNT PAGE WHEN THAT IS SET UP!

    return render_template("register.html")
