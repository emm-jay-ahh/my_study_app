import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


(
    db_user,
    db_pass,
    db_name,
    db_domain
) = (os.environ.get(item) for item in [
    "DB_USER",
    "DB_PASS",
    "DB_NAME",
    "DB_DOMAIN"
    ]
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "books"
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(150), unique=True, nullable=False)
    book_isbn = db.Column(db.Integer(13), unique=True, nullable=False)

    def __init__(self, book_name):
        self.book_name = book_name
    
    def __init__(self, book_isbn):
        self.book_isbn = book_isbn

    @property
    def serialize(self):
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "book_isbn": self.book_isbn
        }

class Course(db.Model):
    __tablename__ = "courses"
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(150), unique=True, nullable=False)
    course_

    def __init__(self, course_name):
        self.course_name = course_name

    @property
    def serialize(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name
        }

class Certification(db.Model):
    __tablename__ = "certifications"
    cert_id = db.Column(db.Integer, primary_key=True)
    cert_name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, cert_name):
        self.cert_name = cert_name

    @property
    def serialize(self):
        return {
            "cert_id": self.cert_id,
            "cert_name": self.cert_name
        }


db.create_all()


@app.route('/', methods=["GET"])
def home():
    return 'Welcome Home!'


@app.route("/books/", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.serialize for book in books])


@app.route('/books/', methods=["POST"])
def add_book():
    new_book = Book(request.json["book_name"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.serialize)


@app.route('/books/<int:id>/', methods=["GET"])
def select_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.serialize)


@app.route('/books/<int:id>/', methods=["PUT", "PATCH"])
def edit_book(id):
    book = Book.query.filter_by(book_id=id)
    book.update(dict(book_name = request.json["book_name"]))
    db.session.commit()
    return jsonify(book.first().serialize)


@app.route('/books/<int:id>/', methods=["DELETE"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(book.serialize)




#####################  ADD LATER
# @app.route('/courses/')
# def view_courses():
#     return 'Courses Library'

# @app.route('/certifications/')
# def view_certifications():
#     return 'Certifications Library'
#####################  ADD LATER


if __name__ == '__main__':
    app.run(debug=True)
