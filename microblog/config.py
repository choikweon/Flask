import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess->default'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pw@db:5432/mbldb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False