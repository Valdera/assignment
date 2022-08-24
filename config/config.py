import os

from dotenv import load_dotenv

load_dotenv('../.env')

DEBUG = True
PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///data.db")
SECRET_KEY = os.environ.get("SECRET_KEY", "example-secret-key")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "example-jwt-secret-key")
PRODUCTION_ENV = os.environ.get("PRODUCTION_ENV", False)
