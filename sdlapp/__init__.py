from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import jwt_manager
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.update(Config)

    db.init_app(app)

    jwt_manager(app)

    from sdlapp.main import main_bp
    app.register_blueprint(main_bp)

    return app
