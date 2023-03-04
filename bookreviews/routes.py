from flask import render_template
from bookreviews import app, db
from bookreviews.models import Book, Role, Teacher, Student, Review


@app.route("/")
def home():
    return render_template("base.html")