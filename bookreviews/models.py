from bookreviews import db


class Book(db.Model):
    # schema for the Book model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_first = db.Column(db.String(30), nullable=False)
    author_surname = db.Column(db.String(50), nullable=False)
    reviews = db.relationship(
        "Review", backref="book", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.title


class Role(db.Model):
    # schema for the user role model
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(25), unique=True)
    teachers = db.relationship(
        "Teacher", backref="role", cascade="all, delete", lazy=True)
    students = db.relationship(
        "Student", backref="role", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.role_name


class Teacher(db.Model):
    # schema for the teacher model
    id = db.Column(db.Integer, primary_key=True)
    prefix = db.Column(db.String(8), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    school = db.Column(db.String(50), nullable=False)
    role = db.Column(
        db.Integer, db.ForeignKey(
            "role.id", ondelete="CASCADE"), nullable=False)
    students = db.relationship(
        "Student", backref="teacher", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} {1}, {2}".format(
            self.prefix, self.surname, self.school
        )


class Student(db.Model):
    # schema for the student model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    surname_initial = db.Column(db.String(2), nullable=False)
    school = db.Column(db.String(50), nullable=False)
    books_read = db.Column(db.Integer)
    role = db.Column(
        db.Integer, db.ForeignKey(
            "role.id", ondelete="CASCADE"), nullable=False)
    teacher = db.Column(
        db.Integer, db.ForeignKey(
            "teacher.id", ondelete="CASCADE"), nullable=False)
    reviews = db.relationship(
        "Review", backref="student", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.first_name + " " + self.surname_initial


class Review(db.Model):
    # schema for the review model
    id = db.Column(db.Integer, primary_key=True)
    reviewer = db.Column(
        db.Integer, db.ForeignKey(
            "student.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    book = db.Column(
        db.Integer, db.ForeignKey(
            "book.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.title
