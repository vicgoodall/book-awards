from flask import (Flask, render_template, session, url_for, redirect,
                   request, flash)
from bookreviews import app, db
from bookreviews.models import Books, Roles, Teachers, Students, Reviews
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    books = list(Books.query.order_by(Books.id).all())
    return render_template("base.html", books=books)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    if "user" in session:
        # if user is already logged in, flash message and redirect to account
        flash("You are already logged in.")
        return redirect(url_for("account", user=session["user"]))
    return render_template("login.html")


# register new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        # if user is already logged in, flash message and redirect to account
        flash("You are already registered.")
        return redirect(url_for("account", user=session["user"]))
    elif request.method == "POST":
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
            student_search = Students.query.filter_by(email=user).first()
            if student_search is not None:
                student = student_search.id
                review_search = Reviews.query.filter_by(reviewer=student)
                return render_template(
                    "account.html", user=session["user"],
                    account_details=student_search, reviews=review_search)
            else:
                return render_template("account.html", user=session["user"],
                                       account_details=1)
    # where user is not logged in, user navigated to login
    elif user is None:
        return render_template("login.html")

    return render_template("account.html")


@app.route("/student-register/<user>", methods=["GET", "POST"])
def registerStudent(user):
    if "user" in session:
        if request.method == "POST":
            student = request.form["email"]
            # first query to check if email already exists
            found_student = Students.query.filter_by(email=student).first()
            if found_student:
                flash("User already exists with this email.")
                return redirect(url_for("registerStudent"))
            # if no email matches, register new user by adding to db
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
                flash("You are now logged in.")
                return redirect(url_for(
                        "account", user=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("loginTeacher"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("loginTeacher"))

    return render_template("login-teacher.html")


@app.route("/login-student", methods=["GET", "POST"])
def loginStudent():
    if request.method == "POST":
        # check if email exists in db
        existing_user = Students.query.filter(Students.email ==
                                              request.form.get(
                                                "email").lower()).all()

        if existing_user:
            print(request.form.get("email"))
            # ensure hashed password matches user input
            if check_password_hash(
              existing_user[0].password, request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("You are now logged in.")
                return redirect(url_for(
                        "account", user=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Email and/or Password")
                return redirect(url_for("login-student"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("loginStudent"))

    return render_template("login-student.html")


@app.route("/logout")
def logout():
    # log the user out of their session
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add-review")
# returns query of books yet to be reviewed by user
def booksNotReviewed():
    if "user" in session:
        user = session["user"]
        student_search = Students.query.filter_by(email=user).first()
        student = student_search.id
        subquery = db.session.query(Reviews.book).filter(
            Reviews.reviewer == student).subquery()
        books_not_reviewed = Books.query.filter(~Books.id.in_(subquery)).all()
        if books_not_reviewed:
            return render_template(
                "add-review.html", books=books_not_reviewed)


@app.route("/add-review", methods=["GET", "POST"])
def addReview():
    # student adds new review
    if request.method == "POST":
        user = session["user"]
        reviewer = Students.query.filter_by(email=user).first()
        review = Reviews(
                reviewer=reviewer.id,
                title=request.form.get("title").lower(),
                rating=request.form.get(
                    "rating"),
                review=request.form.get("review"),
                book=request.form.get("book"),
                author=reviewer.first_name,
                author_initial=reviewer.surname_initial)

        db.session.add(review)
        db.session.commit()
        # every time review is published, increment student's books_read
        reviewer.books_read = reviewer.books_read + 1
        db.session.commit()

        flash("Your review has been published.")
        return redirect(url_for("account", user=session["user"]))

    return render_template("add-review.html")


@app.route("/account/<user>,<student>")
def deleteStudent(user, student):
    del_student = Students.query.filter_by(id=student).first()
    db.session.delete(del_student)
    db.session.commit()
    flash("Account deleted successfully.")
    user = session["user"]
    teacher_search = Teachers.query.filter_by(email=user).first()
    if teacher_search:
        students = Students.query.filter_by(
                    teacher=teacher_search.id).all()
    return redirect(url_for("account", user=session["user"],
                    account_details=teacher_search, students=students))


@app.route("/update-student/<student_id>", methods=["GET", "POST"])
def updateStudent(student_id):
    student = Students.query.filter_by(id=student_id).first()
    if request.method == "POST":
        student.email = request.form.get("email").lower()
        student.first_name = request.form.get("first_name").lower()
        student.surname_initial = request.form.get(
                        "surname_initial").lower()
        db.session.commit()
        flash("Account updated successfully.")
        user = session["user"]
        teacher_search = Teachers.query.filter_by(email=user).first()
        if teacher_search:
            students = Students.query.filter_by(
                        teacher=teacher_search.id).all()
        return redirect(url_for("account", user=session["user"],
                        account_details=teacher_search, students=students))
    return render_template("update-student.html", student=student)


@app.route("/update-teacher/<user>")
def showTeacher(user):
    user = session["user"]
    teacher = Teachers.query.filter_by(email=user).first()
    return render_template("update-teacher.html", teacher=teacher)


@app.route("/update-teacher/<user>", methods=["GET", "POST"])
def updateTeacher(user):
    user = session["user"]
    teacher = Teachers.query.filter_by(email=user).first()
    if request.method == "POST":
        teacher.email = request.form.get("email").lower()
        teacher.prefix = request.form.get("prefix").lower()
        teacher.surname = request.form.get("surname").lower()
        db.session.commit()
        flash("Account updated successfully.")
        return render_template("update-teacher.html", teacher=teacher)
    return render_template("update-teacher.html")


@app.route("/my-reviews/<user>")
def myReviews(user):
    student_search = Students.query.filter_by(email=user).first()
    if student_search is not None:
        student = student_search.id
        review_search = Reviews.query.filter_by(reviewer=student)
        return render_template(
                    "my-reviews.html", user=session["user"],
                    reviews=review_search)


@app.route("/my-reviews/<user>,<review>")
def deleteReview(user, review):
    student_search = Students.query.filter_by(email=user).first()
    review = Reviews.query.filter_by(id=review).first()
    db.session.delete(review)
    # reduce user's book_read count by 1 when deleting review
    student_search.books_read = student_search.books_read - 1
    db.session.commit()
    flash("Review deleted successfully.")
    if student_search is not None:
        student = student_search.id
        review_search = Reviews.query.filter_by(reviewer=student)
    return render_template("my-reviews.html", user=session["user"],
                           reviews=review_search)


@app.route("/update-review/<review>")
def showReview(review):
    review = Reviews.query.filter_by(id=review).first()
    return render_template("update-review.html", review=review)


@app.route("/update-review/<review>", methods=["GET", "POST"])
def updateReview(review):
    review = Reviews.query.filter_by(id=review).first()
    if request.method == "POST":
        review.title = request.form.get("title").lower()
        review.rating = request.form.get("rating").lower()
        review.review = request.form.get("review")
        db.session.commit()
        flash("Review updated successfully.")
        user = session['user']
        return redirect(url_for("myReviews", user=session["user"]))
    return render_template("update-review.html")


@app.route("/view-reviews/<user>")
def showReviews(user):
    # query to find all reviews written by the teacher's students
    user = session['user']
    teacher = Teachers.query.filter_by(email=user).first()
    subquery = db.session.query(Students.id).filter(
            Students.teacher == teacher.id).subquery()
    students_reviews = Reviews.query.filter(
        Reviews.reviewer.in_(subquery)).all()
    return render_template("view-reviews.html", reviews=students_reviews)


@app.route("/view-reviews/<user><student>,<review>")
def deleteStudentReview(user, student, review):
    user = session['user']
    student_search = Students.query.filter_by(id=student).first()
    review = Reviews.query.filter_by(id=review).first()
    db.session.delete(review)
    # reduce user's book_read count by 1 when deleting review
    student_search.books_read = student_search.books_read - 1
    db.session.commit()
    flash("Review deleted successfully.")
    return redirect(url_for('showReviews', user=session["user"]))


@app.route("/reviews")
def reviews():
    reviews = list(Reviews.query.order_by(Reviews.id).all())
    return render_template("reviews.html", reviews=reviews)


@app.route("/admin", methods=["GET", "POST"])
def adminRegister():
    if "user" in session:
        # if user is already logged in, flash message and redirect to account
        flash("You are already registered.")
        return redirect(url_for("account", user=session["user"]))
    elif request.method == "POST":
        user = Admins(
                email=request.form.get("email").lower(),
                password=generate_password_hash(request.form.get("password")))
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful")
        return redirect(url_for("admin.html", user=session["user"]))

    return render_template("admin-register.html")


@app.route("/admin/<user>", methods=["GET", "POST"])
def admin(user):
    roles = list(Roles.query.order_by(Roles.id).all())
    books = list(Books.query.order_by(Books.id).all())
    return render_template("admin.html", roles=roles, books=books)


@app.route("/admin/<user>", methods=["GET", "POST"])
def addRole():
    if request.method == "POST":
        role = Roles(
            role_name=request.form.get("role_name").lower())
        db.session.add(role)
        db.session.commit()
    return redirect(url_for('admin', user=session['user']))


@app.route("/admin/<user>", methods=["GET", "POST"])
def addBooks():
    if request.method == "POST":
        book = Books(
                title=request.form.get("title").lower(),
                author_first=request.form.get("author_first").lower(),
                author_surname=request.form.get("author_surname").lower())
        db.session.add(book)
        db.session.commit()
    return redirect(url_for('admin', user=session['user']))
