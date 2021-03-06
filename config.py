__author__ = 'suren'
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'can never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://pi_user:raspberry@localhost/FB_DATABASE_V01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False