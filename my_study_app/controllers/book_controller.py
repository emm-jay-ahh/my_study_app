from flask import Blueprint, jsonify, request, render_template
from main import db
from models.books import Book
from schemas.book_schema import books_schema, book_schema


books = Blueprint('books', __name__)

# @app.route('/', methods=["GET"])
#     def home():
#         return "Welcome to 'My Study App'"


@books.route("/books/", methods=["GET"])
def get_books():
    data = {
    "page_title": "Book Index",
    "books": books_schema.dump(Book.query.all())
    }
    return render_template("book_index.html", page_data = data)


@books.route("/books/", methods=["POST"])
def create_book():
    new_book=book_schema.load(request.form)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(book_schema.dump(new_book))


@books.route("/books/<int:id>/", methods = ["GET"])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book_schema.dump(book))


@books.route("/books/<int:id>/", methods=["PUT", "PATCH"])
def update_book(id):
    book = Book.query.filter_by(book_id=id)
    updated_fields = book_schema.dump(request.json)
    if updated_fields:
        book.update(updated_fields)
        db.session.commit()
    return jsonify(book_schema.dump(book.first()))


@books.route("/books/<int:id>/", methods = ["DELETE"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(book_schema.dump(book))