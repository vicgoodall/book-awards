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
        existing_user = Teacher.query.filter_by
        (Teacher.username == request.form.get("username").lower())

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        username = Teacher(username=request.form.get("username").lower())
        prefix = Teacher(prefix=request.form.get("prefix").lower())
        surname = Teacher(surname=request.form.get("surname").lower())
        school = Teacher(school=request.form.get("school").lower())
        password = generate_password_hash(request.form.get("password"))
        db.session.add(username)
        db.session.add(prefix)
        db.session.add(surname)
        db.session.add(school)
        db.session.add(password)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
    return render_template("register.html")
