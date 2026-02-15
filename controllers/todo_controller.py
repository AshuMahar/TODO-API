from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from extensions import mongodb

@jwt_required()
def create_todo():
    user_id = get_jwt_identity()
    data = request.get_json()
    todo = {
        "user_id": ObjectId(user_id),
        "title": data["title"],
        "desc": data.get("desc", ""),
        "is_complete": False
    }
    mongodb.db.todos.insert_one(todo)
    return {"message": "Todo created"}, 201

@jwt_required()
def get_todos():
    user_id = get_jwt_identity()
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 5))
    skip = (page - 1) * limit

    query = {"user_id": ObjectId(user_id)}
    todos = mongodb.db.todos.find(query).skip(skip).limit(limit)

    result = []
    for t in todos:
        result.append({
            "id": str(t["_id"]),
            "title": t["title"],
            "desc": t.get("desc", ""),
            "is_complete": t["is_complete"]
        })

    return {
        "page": page,
        "limit": limit,
        "todos": result
    }
