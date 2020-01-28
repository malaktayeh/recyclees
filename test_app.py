import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Donors, Donees, Items

token = os.environ['TOKEN']
user_id = 1

class RecycleesTestCase(unittest.TestCase):
    """This class represents the recyclees test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.headers = {
            'Content-Type': 'application/json', 
            'authorization': 'Bearer {}'.format(token)
        }
        self.database_name = "recyclees_test"
        self.database_path = "postgresql://{}@{}/{}".\
            format('postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        pass

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_item = {
            "brand":"Apple",
            "category":"Laptops",
            "condition":"Used",
            "delivery":"True",
            "description":"Will ship in original packaging.",
            "item_name":"MacBook Pro"
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # /////////////////////////////////////////////////////////////////
    # 
    # Tests for public route
    # 
    # /////////////////////////////////////////////////////////////////

    def test_get_ten_items_from_public_route(self):
        res = self.client().get('/api/public')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['items']) > -1)


    def test_404_fail_to_get_item_list(self):
        res = self.client().get('/api/public/items')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    # /////////////////////////////////////////////////////////////////
    # 
    # Tests for donor routes
    # 
    # /////////////////////////////////////////////////////////////////

    # GET ROUTE
    def test_get_list_of_items_posted_by_donor(self):
        res = self.client().get('/api/donors/1/items', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsInstance(data['items'], list)
        self.assertEqual(data['items'][0] is not None, data['items'][0]['donor'] is 1)

    def test_401_is_donor_authorized_to_get_own_list_of_items(self):
        res = self.client().get('/api/donors/1/items', headers={'Content-Type': 'application/json'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

        # POST ROUTE
    # def test_donor_adds_new_items_to_database(self):
    #     res = self.client().post('/api/donors/1/items', headers=self.headers, json=self.new_item)
    #     data = json.loads(res.data)

    #     print(data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
        # self.assertEqual(data['item'][0]['donor'], 1)
        # self.assertEqual(data['item'][0]['item_name'], self.new_item['item_name'])




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()