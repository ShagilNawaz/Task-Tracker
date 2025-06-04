from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    CORS(app)
    db.init_app(app)

    from .routes import main
    from .auth import auth_bp

    app.register_blueprint(main)
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app