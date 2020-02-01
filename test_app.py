import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Donors, Donees, Items

token = os.environ['TOKEN']
class RecycleesTestCase(unittest.TestCase):
    """This class represents the recyclees test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.headers = {
            "Content-Type": "application/json", 
            "authorization": "Bearer {}".format(token)
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
        
        self.new_item2 = {
            "brand":"Lenovo",
            "category":"Laptops",
            "condition":"Used",
            "delivery":"True",
            "description":"Will ship in original packaging.",
            "item_name":"Lenovo Yoga Tablet"
        }

        self.incomplete_item = {
            "brand":"test",
            "description":"test",
            "item_name":"test"
        }

        self.new_donor = {
            "user_name":"Tiffany1!XD",
            "first_name":"Tiffany",
            "last_name":"Smith",
            "city":"Dearborn",
            "state":"Michigan"
        }

        self.new_donee = {
            "user_name":"AAANY!XD",
            "first_name":"Jeniffer",
            "last_name":"Newboard",
            "city":"Toronto",
            "state":"ON"
        }

        self.new_donee_missing_data = {
            "user_name":"dertlws2",
            "first_name":"Tiffany",
            "last_name":"Smith",
            "state":"Michigan"
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
    # def test_donor_adds_new_item(self):
    #     res = self.client().post('/api/donors/1/items', headers=self.headers, json=self.new_item2)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['item']['donor'], 1)
    #     self.assertEqual(data['item']['item_name'], self.new_item['item_name'])

    # def test_400_donor_adding_incomplete_item(self):
    #     res = self.client().post('api/donors/1/items', headers=self.headers, json=self.incomplete_item)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "Unprocessable")

    # DELETE ROUTE
    # def test_donor_tries_to_deletes_item(self):
    #     res = self.client().delete('api/donors/2/items/1', headers=self.headers)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['item'][1]['id'][1], 1)

    # def test_404_donor_tries_to_delete_nonexistent_item(self):
    #     res = self.client().delete('api/donors/2/items/10000', headers=self.headers)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Not found')

    # # PATCH ROUTE
    # def test_donor_updates_current_item(self):
    #     res = self.client().patch('/api/donors/1/items/1', headers=self.headers, json=self.new_item)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['updated_item']['item_name'], self.new_item['item_name'])
    #     self.assertEqual(data['updated_item']['brand'], self.new_item['brand'])
    #     self.assertEqual(data['updated_item']['category'], self.new_item['category'])
    #     self.assertEqual(data['updated_item']['condition'], self.new_item['condition'])
    #     self.assertEqual(data['updated_item']['delivery'], self.new_item['delivery'])

    # def test_400_donor_tries_to_update_current_item(self):
    #     res = self.client().patch('/api/donors/2/items/1', headers=self.headers, json=self.incomplete_item)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], "Bad request")


    # /////////////////////////////////////////////////////////////////
    # 
    # Tests for admin routes
    # 
    # /////////////////////////////////////////////////////////////////

    # POST Donor route
    # def test_add_donor_to_database(self):
    #     res = self.client().post('/api/donors', headers=self.headers, json=self.new_donor)
    #     data = json.loads(res.data)
    #     does_item_with_id_exist = Donors.query.filter(Donors.id == data['new_donor_id']).first()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['new_donor']['user_name'], self.new_donor['user_name'])
    #     self.assertEqual(data['new_donor']['first_name'], self.new_donor['first_name'])
    #     self.assertEqual(data['new_donor']['last_name'], self.new_donor['last_name'])
    #     self.assertEqual(data['new_donor']['city'], self.new_donor['city'])
    #     self.assertEqual(data['new_donor']['state'], self.new_donor['state'])
    #     self.assertTrue(does_item_with_id_exist)

    def test_422_donor_could_not_be_added_to_database(self):
        res = self.client().post('/api/donors', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Bad request")

    # POST Donee route
    # def test_add_donee_to_database(self):
    #     res = self.client().post('/api/donees', headers=self.headers, json=self.new_donee)
    #     data = json.loads(res.data)
    #     does_item_with_id_exist = Donees.query.filter(Donees.id == data['new_donee_id']).first()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['new_donee']['user_name'], self.new_donee['user_name'])
    #     self.assertEqual(data['new_donee']['first_name'], self.new_donee['first_name'])
    #     self.assertEqual(data['new_donee']['last_name'], self.new_donee['last_name'])
    #     self.assertEqual(data['new_donee']['city'], self.new_donee['city'])
    #     self.assertEqual(data['new_donee']['state'], self.new_donee['state'])
    #     self.assertTrue(does_item_with_id_exist)

    def test_400_donee_could_not_be_added_to_database(self):
        res = self.client().post('/api/donees', headers=self.headers, json=self.new_donee_missing_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unprocessable")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()