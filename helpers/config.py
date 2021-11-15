import os

class Config(object):
  DEBUG = False
  TESTING = False
  BASE_DIR_API = os.environ.get("BASE_DIR_API")
  BASE_DIR_LOGS = os.environ.get("BASE_DIR_LOGS")
  BASE_DIR_GEO = os.environ.get("BASE_DIR_GEO")
  BASE_DIR_COUNTRIES = os.environ.get("BASE_DIR_COUNTRIES")
  BASE_DIR_ALMILLON = os.environ.get("BASE_DIR_ALMILLON")
  BASE_DIR_ESTRUCTURAL = os.environ.get("BASE_DIR_ESTRUCTURAL")
  BASE_DIR_METAL = os.environ.get("BASE_DIR_METAL")
  POSTGRESQL_HOST = os.environ.get("POSTGRESQL_HOST")
  POSTGRESQL_DB = os.environ.get("POSTGRESQL_DB")
  POSTGRESQL_USER = os.environ.get("POSTGRESQL_USER")
  POSTGRESQL_PWD = os.environ.get("POSTGRESQL_PWD")
  JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
  JWT_HEADER_NAME = os.environ.get("JWT_HEADER_NAME")
  JWT_ACCESS_TOKEN_EXPIRES = os.environ.get("JWT_ACCESS_TOKEN_EXPIRES")
  TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
  TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
  TWILIO_NUM = os.environ.get("TWILIO_NUM")
  TWILIO_WSSP = os.environ.get("TWILIO_WSSP")
  EMAIL_HOST = os.environ.get("EMAIL_HOST")
  EMAIL_PORT = os.environ.get("EMAIL_PORT")
  PAGINATION_START = os.environ.get("PAGINATION_START")
  PAGINATION_LIMIT = os.environ.get("PAGINATION_LIMIT")

class DevelopmentConfig(Config):
  ENV = "development"
  DEVELOPMENT = True
  SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
  DEBUG = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False