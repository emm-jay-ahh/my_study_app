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
        # we use the client to make a request
        response = self.client.get("/books/")
        # Now we can perform tests on the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Book Index</h1>', response.data)
    
    def test_create_bad_book(self):
        response = self.client.post("/books/", data={"book_name": ""})
        self.assertEqual(response.status_code, 400)

    def test_create_good_book(self):
        response = self.client.post("/books/", data={"book_name": "testbook"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["book_name"], "testbook")
        self.client.delete(f"/books/{response.get_json()['book_id']}/")

    def test_delete_book(self):
        response1 = self.client.post("/books/", data={"book_name": "testbook"})
        id = response1.get_json()["book_id"]
        
        response2 = self.client.delete(f"/books/{id}/")
        self.assertEqual(response2.status_code, 200)

    def test_update_book(self):
        # create the resource to test
        response1 = self.client.post("/books/", data={"book_name": "testbook"})
        id = response1.get_json()["book_id"]

        # change the resource and check the changes were successful
        response2 = self.client.put(f"/books/{id}/", json={"book_name": "newtestbook"})
        self.assertEqual(response2.status_code, 200)
        data = response2.get_json()
        self.assertEqual(data["book_name"], "newtestbook")

        # clean up the resource afterwards
        self.client.delete(f"/books/{id}/")