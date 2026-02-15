from flask import Blueprint
from controllers.auth_controller import register, login, profile

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/api/v1/auth/register", methods=["POST"])(register)
auth_bp.route("/api/v1/auth/login", methods=["POST"])(login)
auth_bp.route("/api/v1/auth/profile", methods=["GET"])(profile)
