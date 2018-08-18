__author__ = 'suren'
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'can never guess'
