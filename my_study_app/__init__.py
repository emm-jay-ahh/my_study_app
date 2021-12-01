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


@app.route('/', methods=["GET"])
def home():
    return 'Welcome Home!'


@app.route("/books/", methods=["GET"])
def book_index():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return jsonify(books)


@app.route('/books/', methods=["POST"])
def add_book():
    sql = f"INSERT INTO books (title) VALUES ('{request.json['title']}');"
    cursor.execute(sql)
    connection.commit()

    sql = "SELECT * FROM books ORDER BY ID DESC LIMIT 1"
    cursor.execute(sql)
    book = cursor.fetchone()
    return jsonify(book)


@app.route('/books/<int:id>/', methods=["GET"])
def select_book(id):
    sql = f"SELECT * FROM books WHERE id = {id}"
    cursor.execute(sql)
    book = cursor.fetchone()
    return jsonify(book)


@app.route('/books/<int:id>/', methods=["PUT", "PATCH"])
def edit_book(id):
    sql = f"UPDATE books SET title = '{request.json['title']}' WHERE id = {id};"
    cursor.execute(sql)
    connection.commit()

    sql = f"SELECT * FROM books WHERE id = {id}"
    cursor.execute(sql)
    book = cursor.fetchone()
    return jsonify(book)


@app.route('/books/<int:id>/', methods=["DELETE"])
def delete_book(id):
    sql = f"SELECT * FROM books WHERE id = {id};"
    cursor.execute(sql)
    book = cursor.fetchone()

    if book:
        sql = f"DELETE FROM books WHERE id = {id};"
        cursor.execute(sql)
        connection.commit()

    return jsonify(book)


# @app.route('/courses/')
# def view_courses():
#     return 'Courses Library'

# @app.route('/certifications/')
# def view_certifications():
#     return 'Certifications Library'

if __name__ == '__main__':
    app.run(debug=True)
