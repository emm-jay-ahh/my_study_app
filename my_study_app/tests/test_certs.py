import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"]="testing"

class TestCerts(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_cert_index(self):
        response = self.client.get("/certs/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_create_bad_cert(self):
        response = self.client.post("/certs/", json={"cert_name": ""})
        self.assertEqual(response.status_code, 400)