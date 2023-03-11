from bookreviews import db


class Books(db.Model):
    # schema for the Book model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_first = db.Column(db.String(30), nullable=False)
    author_surname = db.Column(db.String(50), nullable=False)
    reviews = db.relationship(
        "Reviews", backref="book_reviewed", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.title


class Roles(db.Model):
    # schema for the user role model
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(25), unique=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.role_name


class Teachers(db.Model):
    # schema for the teacher model
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    prefix = db.Column(db.String(8), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    school = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(
        db.Integer, db.ForeignKey(
            "roles.id", ondelete="CASCADE"), nullable=False)
    students = db.relationship(
        "Students", backref="their_teacher", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} {1}, {2}".format(
            self.prefix, self.surname, self.school
        )


class Students(db.Model):
    # schema for the student model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    surname_initial = db.Column(db.String(2), nullable=False)
    school = db.Column(db.String(50), nullable=False)
    books_read = db.Column(db.Integer)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(
        db.Integer, db.ForeignKey(
            "roles.id", ondelete="CASCADE"), nullable=False)
    teacher = db.Column(
        db.Integer, db.ForeignKey(
            "teachers.id", ondelete="CASCADE"), nullable=False)
    reviews = db.relationship(
        "Reviews", backref="review_author", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.first_name + " " + self.surname_initial


class Reviews(db.Model):
    # schema for the review model
    id = db.Column(db.Integer, primary_key=True)
    reviewer = db.Column(
        db.Integer, db.ForeignKey(
            "students.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    book = db.Column(
        db.Integer, db.ForeignKey(
            "books.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.title
