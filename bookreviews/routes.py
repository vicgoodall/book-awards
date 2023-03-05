from flask import render_template
from bookreviews import app, db
from bookreviews.models import Book, Role, Teacher, Student, Review
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")
