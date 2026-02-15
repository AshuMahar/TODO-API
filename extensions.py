from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

mongodb = PyMongo()
jwt = JWTManager()
