__author__ = 'suren'
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.VARCHAR(64), index=True, unique=True)
    email = db.Column(db.VARCHAR(120), index=True, unique=True)
    password_hash = db.Column(db.VARCHAR(128))
    posts = db.relationship('Log', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# class TempTable(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fname = db.Column(db.VARCHAR(4))

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class tempt(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      fname = db.Column(db.VARCHAR(4))