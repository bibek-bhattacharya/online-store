import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

# Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data/db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False