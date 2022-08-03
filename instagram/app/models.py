from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    pk = db.Column(db.Integer, nullable=True, index=True)
    username = db.Column(db.String(64), nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    verification_code = db.Column(db.String(128), nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.username})'

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute!')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
