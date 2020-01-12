import os

from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

# database_path = os.environ['DATABASE_URL']
database_path = 'postgresql://postgres@localhost:5432/recyclees'
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


'''
Donor
'''

class Donors(db.Model):  
    __tablename__ = 'Donors'

    id = Column(db.Integer, primary_key=True)
    user_name = Column(db.String(30), nullable=False, unique=True)
    first_name = Column(db.String(20), nullable=False)
    last_name = Column(db.String(30), nullable=False)
    state = Column(db.String, nullable=False)
    city = Column(db.String, nullable=False)
    items = db.relationship('Items', backref='list', lazy=True)

    def __init__(self, user_name, first_name, last_name, state, city):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.state = state
        self.city = city


    def format(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'state': self.state,
            'city': self.city,
            'items': self.items
        }


'''
Donee
'''

class Donees(db.Model):  
    __tablename__ = 'Donees'

    id = Column(db.Integer, primary_key=True)
    user_name = Column(db.String(30), nullable=False, unique=True)
    first_name = Column(db.String(20), nullable=False)
    last_name = Column(db.String(30), nullable=False)
    state = Column(db.String, nullable=False)
    city = Column(db.String, nullable=False)
    organization = Column(db.String(100))
    item = db.Column(db.Integer, db.ForeignKey('Items.id'), nullable=False)

    def __init__(self, user_name, first_name, last_name, state, city, organization):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.state = state
        self.city = city
        self.organization = organization


    def format(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'state': self.state,
            'city': self.city,
            'organization': self.organization
        }

'''
Item
'''

class Items(db.Model):  
    __tablename__ = 'Items'

    id = Column(db.Integer, primary_key=True)
    item_name = Column(db.String(50), nullable=False)
    brand = Column(db.String(30), nullable=False)
    category = Column(db.String(30), nullable=False)
    condition = Column(db.String(30), nullable=False)
    description = Column(db.String(1000), nullable=False)
    delivery = Column(db.Boolean, nullable=False, default=False)
    location = Column(db.String, nullable=False)
    donor = db.Column(db.String(), db.ForeignKey('Donors.user_name'), nullable=False)
    donee = db.relationship('Donees', backref='list', lazy=True)


    def __init__(self, item_name, brand, category, condition, description, delivery, location):
        self.item_name = item_name,
        self.brand = brand,
        self.category = category,
        self.condition = condition,
        self.description = description,
        self.delivery = delivery,
        self.location = location


    def format(self):
        return {
            'item_name': self.item_name,
            'brand': self.brand,
            'category': self.category,
            'condition': self.condition,
            'description': self.description,
            'delivery': self.delivery,
            'location': self.location
        }