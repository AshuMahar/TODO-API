from flask import Flask
from dotenv import load_dotenv
import os
from extensions import mongodb, jwt
from routes.auth_routes import auth_bp
from routes.todo_routes import todo_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Load config from environment
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    # Initialize extensions
    mongodb.init_app(app)
    jwt.init_app(app)

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
