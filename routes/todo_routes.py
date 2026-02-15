from flask import Blueprint
from controllers.todo_controller import create_todo, get_todos, update_todo, delete_todo

todo_bp = Blueprint("todos", __name__)

todo_bp.route("/api/v1/todos", methods=["POST"])(create_todo)
todo_bp.route("/api/v1/todos", methods=["GET"])(get_todos)
todo_bp.route("/api/v1/todos/<todo_id>", methods=["PUT"])(update_todo)
todo_bp.route("/api/v1/todos/<todo_id>", methods=["DELETE"])(delete_todo)
