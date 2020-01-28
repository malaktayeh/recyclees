import os
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

# database_path = os.environ['DATABASE_URL']
database_path = 'postgresql://postgres@localhost:5432/recyclees_test'
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


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

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
    items = db.relationship('Items', backref='donors',
                            cascade='all, delete-orphan', lazy=True)

    def __repr__(self):
        return f'<Donor {self.id} {self.user_name} {self.first_name} \
                 {self.last_name} {self.state} {self.city} >'

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

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


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
    organization = Column(db.String(100), nullable=True)
    items = db.relationship('Items', backref='donees', cascade='all',
                            lazy=True)

    def __repr__(self):
        return f'<Donee {self.id} {self.user_name} {self.first_name} \
                 {self.last_name} {self.state} {self.city} \
                 {self.organization} >'

    def __init__(self, user_name, first_name, last_name, state,
                 city, organization):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.organization = organization

    def format(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'state': self.state,
            'city': self.city,
            'organization': self.organization,
            'items': self.items
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


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
    delivery = Column(db.String(5), nullable=False, default=False)
    donor = db.Column(db.Integer, db.ForeignKey
                      ('Donors.id', ondelete='cascade'), nullable=False)
    donee = db.Column(db.Integer, db.ForeignKey('Donees.id'))

    def __repr__(self):
        return f'< Item id: {self.id} {self.item_name} {self.brand} \
                {self.category} {self.condition} {self.description} \
                {self.delivery} {self.donor} {self.donee}>'

    def __init__(self, **kwargs):
        super(Items, self).__init__(**kwargs)

    def format(self):
        return {
            'id': self.id,
            'item_name': self.item_name,
            'brand': self.brand,
            'category': self.category,
            'condition': self.condition,
            'description': self.description,
            'delivery': self.delivery,
            'donor': self.donor,
            'donee': self.donee
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
