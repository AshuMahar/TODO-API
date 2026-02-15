from flask import Blueprint
from controllers.todo_controller import create_todo, get_todos

todo_bp = Blueprint("todos", __name__)

todo_bp.route("/api/v1/todos", methods=["POST"])(create_todo)
todo_bp.route("/api/v1/todos", methods=["GET"])(get_todos)
