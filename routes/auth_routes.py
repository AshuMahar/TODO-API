from flask import Blueprint
from controllers.auth_controller import register, login, profile, refresh, logout

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/api/v1/auth/register", methods=["POST"])(register)
auth_bp.route("/api/v1/auth/login", methods=["POST"])(login)
auth_bp.route("/api/v1/auth/profile", methods=["GET"])(profile)
auth_bp.route("/api/v1/auth/refresh", methods=["POST"])(refresh)
auth_bp.route("/api/v1/auth/logout", methods=["POST"])(logout)
