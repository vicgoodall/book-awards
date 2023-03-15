from flask import (Flask, render_template, session, url_for, redirect,
                   request, flash)
from bookreviews import app, db
from bookreviews.models import Books, Roles, Teachers, Students, Reviews
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/login")
def login():
    return render_template("login.html")


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
            user = Teachers(
                email=request.form.get("email").lower(),
                prefix=request.form.get("prefix").lower(),
                surname=request.form.get("surname").lower(),
                school=request.form.get("school").lower(),
                role=1,
                password=generate_password_hash(request.form.get("password")))

            db.session.add(user)
            db.session.commit()

        # put the new user into 'session' cookie
            session["user"] = request.form.get("email").lower()
            flash("Registration Successful")
            return redirect(url_for("account", user=session["user"]))

    return render_template("register.html")


@app.route("/account/<user>", methods=["GET", "POST"])
def account(user):
    # provide user details for the account page
    if "user" in session:
        teacher_search = Teachers.query.filter_by(email=user).first()
        if teacher_search:
            students = Students.query.filter_by(
                teacher=teacher_search.id).all()
            return render_template(
                "account.html", user=session["user"],
                account_details=teacher_search, students=students)
        else:
            student_search = Students.query.filter_by(username=user).first()
            return render_template(
                "account.html", user=session["user"],
                account_details=student_search)
    # where user is not logged in, user navigated to login
    else:
        return render_template("login.html")

    return render_template("account.html")


@app.route("/student-register/<user>", methods=["GET", "POST"])
def registerStudent(user):
    if "user" in session:
        if request.method == "POST":
            student = request.form["username"]
            # first query to check if username already exists
            found_student = Students.query.filter_by(username=student).first()
            if found_student:
                flash("User already exists with this username.")
                return redirect(url_for("student-register"))
            # if no username matches, register new user by adding to db
            else:
                user = session["user"]
                teacher = Teachers.query.filter_by(email=user).first()
                student = Students(
                    email=request.form.get("email").lower(),
                    first_name=request.form.get("first_name").lower(),
                    surname_initial=request.form.get(
                        "surname_initial").lower(),
                    school=teacher.school,
                    role=2,
                    books_read=0,
                    teacher=teacher.id,
                    password=generate_password_hash(
                        request.form.get("password")))

                db.session.add(student)
                db.session.commit()

            flash("Registration Successful")
            return redirect(url_for("account", user=session["user"]))

    return render_template("student-register.html")


@app.route("/login-teacher", methods=["GET", "POST"])
def loginTeacher():
    if request.method == "POST":
        # check if email exists in db
        existing_user = Teachers.query.filter(Teachers.email ==
                                              request.form.get(
                                                "email").lower()).all()

        if existing_user:
            print(request.form.get("email"))
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user[0].password, request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Welcome, {}".format(request.form.get("email")))
                return redirect(url_for(
                        "account", email=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login-teacher"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login-teacher"))

    return render_template("login-teacher.html")


@app.route("/login-student", methods=["GET", "POST"])
def loginStudent():
    if request.method == "POST":
        # check if email exists in db
        existing_user = Students.query.filter(Students.username ==
                                              request.form.get(
                                                "email").lower()).all()

        if existing_user:
            print(request.form.get("email"))
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user[0].password, request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Welcome, {}".format(request.form.get("email")))
                return redirect(url_for(
                        "account", email=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login-student"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login-student"))

    return render_template("login-student.html")
