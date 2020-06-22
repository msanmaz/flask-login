from . import db
import datetime
from sqlalchemy import Column, Integer, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(140), unique=True)
    password_has = db.Column(db.String(140))
    name = db.Column(db.String(140))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    posts = db.relationship('Post', backref= 'author',lazy='dynamic')
    def set_password(self, password):
        self.password_has = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_has,password)

    
    
    def __repr__(self):
        return '<User %r>' % self.name


class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name


class Post(db.Model):
    __tablename__='post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __repr__(self):
        return '<Post %r>' % (self.body)