import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"]="testing"

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_book_index(self):
        response = self.client.get("/books/")
        data = response.get_json()
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_create_bad_book(self):
        response = self.client.post("/books/", json={"book_name": ""})
        self.assertEqual(response.status_code, 400)    