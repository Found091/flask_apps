from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(basedir, '.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL', 'sqlite:///' + path.join(basedir, 'data.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    LOG_FILE = 'application.log'
