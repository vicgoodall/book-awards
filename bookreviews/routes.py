from flask import (Flask, render_template, session, url_for, redirect,
                   request, flash)
from bookreviews import app, db
from bookreviews.models import Book, Role, Teacher, Student, Review
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        # name_attempt = request.form.get("username").lower()
        # if (Teacher.query().filter_by(
        # username == name_attempt)) is not None:

        user = request.form["email"]
        found_user = Teacher.query.filter_by(email=user).first()
        if found_user:
            flash("User already exists with this email address.")
            return redirect(url_for("register"))
        else:
            new_user = Teacher(
                email=request.form.get("email").lower(),
                prefix=request.form.get("prefix").lower(),
                surname=request.form.get("surname").lower(),
                school=request.form.get("school").lower(),
                password=generate_password_hash(request.form.get("password")))

            db.session.add(new_user)
            db.session.commit()

        # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful")
            return redirect(url_for("account", email=session["email"]))
    return render_template("register.html")
