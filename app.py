from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from extensions import mongodb, jwt
from routes.auth_routes import auth_bp
from routes.todo_routes import todo_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for all routes
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://localhost:5173", "https://*"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Load config from environment
    mongo_uri = os.getenv("MONGO_URI")
    jwt_secret = os.getenv("JWT_SECRET_KEY")

    if mongo_uri:
        app.config["MONGO_URI"] = mongo_uri
        try:
            mongodb.init_app(app)
        except Exception:
            pass
    
    if jwt_secret:
        app.config["JWT_SECRET_KEY"] = jwt_secret
    
    try:
        jwt.init_app(app)
    except Exception:
        pass

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        token = mongodb.db.token_blacklist.find_one({"jti": jti})
        return token is not None

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
