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
        # we use the client to make a request
        response = self.client.get("/certs/")
        # Now we can perform tests on the response
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Cert Index</h1>', response.data)
    
    def test_create_bad_cert(self):
        response = self.client.post("/certs/", data={"cert_name": ""})
        self.assertEqual(response.status_code, 400)

    def test_create_good_cert(self):
        response = self.client.post("/certs/", data={"cert_name": "testcert"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["cert_name"], "testcert")
        self.client.delete(f"/certs/{response.get_json()['cert_id']}/")

    def test_delete_cert(self):
        response1 = self.client.post("/certs/", data={"cert_name": "testcert"})
        id = response1.get_json()["cert_id"]
        
        response2 = self.client.delete(f"/certs/{id}/")
        self.assertEqual(response2.status_code, 200)

    def test_update_cert(self):
        # create the resource to test
        response1 = self.client.post("/certs/", data={"cert_name": "testcert"})
        id = response1.get_json()["cert_id"]

        # change the resource and check the changes were successful
        response2 = self.client.put(f"/certs/{id}/", json={"cert_name": "newtestcert"})
        self.assertEqual(response2.status_code, 200)
        data = response2.get_json()
        self.assertEqual(data["cert_name"], "newtestcert")

        # clean up the resource afterwards
        self.client.delete(f"/certs/{id}/")