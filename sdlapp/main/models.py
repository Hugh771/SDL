from sdlapp import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwd_hash = db.Column(db.String(128), unique=True, nullable=False)
    role = db.Column(db.String(80), default='active')
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    phone_number = db.Column(db.String(20), nullable=True)
    api_key = db.Column(db.String(128), nullable=True)
    custom_attributes = db.Column(db.JSON, nullable=True)
    def __repr__(self):
        return '<User %r>' %self.username