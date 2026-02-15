from flask import Flask
from dotenv import load_dotenv
import logging
import os
from extensions import mongodb, jwt
from routes.auth_routes import auth_bp
from routes.todo_routes import todo_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Load config from environment
    mongo_uri = os.getenv("MONGO_URI")
    jwt_secret = os.getenv("JWT_SECRET_KEY")

    if mongo_uri:
        app.config["MONGO_URI"] = mongo_uri
        try:
            mongodb.init_app(app)
        except Exception:
            logging.exception("Failed to initialize MongoDB with provided MONGO_URI")
    else:
        logging.warning("MONGO_URI not set — skipping MongoDB initialization. DB features will be disabled until set.")

    if jwt_secret:
        app.config["JWT_SECRET_KEY"] = jwt_secret
    else:
        logging.warning("JWT_SECRET_KEY not set — JWT features will be disabled until set.")

    # Initialize JWT (safe to call even if secret missing; errors will surface when used)
    try:
        jwt.init_app(app)
    except Exception:
        logging.exception("Failed to initialize JWT extension")

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(todo_bp)

    # Basic health endpoint for platforms' health checks
    @app.route("/")
    def index():
        return {"status": "ok"}, 200

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
