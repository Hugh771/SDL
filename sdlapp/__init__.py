from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sdlapp.auth.auth import jwt
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.update(Config)

    db.init_app(app)
    db.create_all()
    jwt.init_app(app)

    from sdlapp.main import main_bp
    app.register_blueprint(main_bp)

    return app
