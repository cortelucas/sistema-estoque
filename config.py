import os
import random, string


class Config(object):
  CSRF_ENABLED = True
  SECRET = '87725E7FC56B98E656AB7A4AEF9D01CAAA625FCF2F7133A48AD42F500E939884'
  TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  APP = None


class DevelopmentConfig(Config):
  TESTING = False
  DEBUG = True
  IP_HOST = 'localhost'
  PORT_HOST = 8000
  URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
  SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://lucas@localhost:3306/sistema-estoque'


class TestingConfig(Config):
  TESTING = True
  DEBUG = True
  IP_HOST = 'localhost'  # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
  PORT_HOST = 5000
  URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


class ProductionConfig(Config):
  DEBUG = False
  TESTING = False
  IP_HOST = 'localhost'  # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
  PORT_HOST = 8080
  URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)


app_config = {
  'development': DevelopmentConfig(),
  'testing': TestingConfig(),
  'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')
