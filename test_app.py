import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Donors, Donees, Items


class RecycleesTestCase(unittest.TestCase):
    """This class represents the recyclees test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "recyclees"
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

        # self.new_question = {
        #     'id': 11,
        #     'question': "What boxer's original name is Cassius Clay?",
        #     'answer': 'Muhammad Ali',
        #     'difficulty:': 1,
        #     'category': 5
        # }

    def tearDown(self):
        """Executed after reach test"""
        pass

    # /////////////////////////////////////////////////////////////////
    # 
    # Tests for public route
    # 
    # /////////////////////////////////////////////////////////////////

    def test_get_ten_items_from_public_route(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['items'])
        self.assertTrue(len(data['categories']) > -1)


    # /////////////////////////////////////////////////////////////////
    # 
    # Tests for donor routes
    # 
    # /////////////////////////////////////////////////////////////////


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()