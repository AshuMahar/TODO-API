from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
from extensions import mongodb

def register():
    data = request.get_json()
    user = {
        "name": data["name"],
        "email": data["email"],
        "password": generate_password_hash(data["password"])
    }
    mongodb.db.users.insert_one(user)
    return {"message": "User registered"}, 201

def login():
    data = request.get_json()
    user = mongodb.db.users.find_one({"email": data["email"]})
    if not user or not check_password_hash(user["password"], data["password"]):
        return {"message": "Invalid credentials"}, 401
    
    access = create_access_token(identity=str(user["_id"]))
    refresh = create_refresh_token(identity=str(user["_id"]))
    
    return {
        "access_token": access,
        "refresh_token": refresh
    }

@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = mongodb.db.users.find_one({"_id": ObjectId(user_id)}, {"password": 0})
    if not user:
        return {"message": "User not found"}, 404
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }
