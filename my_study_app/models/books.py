from main import db


class Book(db.Model):
    __tablename__ = "books"
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, book_name):
        self.book_name = book_name