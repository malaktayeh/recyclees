import os

from sqlalchemy import Column, String, create_engine
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

class Donor(db.Model):  
    __tablename__ = 'Donor'

    id = Column(db.Integer, primary_key=True)
    user_name = Column(db.String)
    first_name = Column(db.String)
    last_name = Column(db.String)
    state = Column(db.String)
    city = Column(db.String)


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
            'city': self.city
        }
