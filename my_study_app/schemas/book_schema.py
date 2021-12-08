from main import ma 
from models.books import Book
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length


class BookSchema(ma.SQLAlchemyAutoSchema):
    book_id = auto_field(dump_only=True)
    book_name = auto_field(required=True, validate=Length(min=1))
    
    class Meta:
        model = Book
        load_instance = True
        
book_schema = BookSchema()
books_schema = BookSchema(many=True)