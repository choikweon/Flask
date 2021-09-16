from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class Mbluser(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), index=True, unique=True)
    email=db.Column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(128))
    posts=db.relationship('Post', backref='author', lazy='dynamic')
    about_me=db.Column(db.String(140))
    last_seen=db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self,size): #C/ wait we don't have size here
        #C/ let's just waste it
        digest=md5(self.email.lower().encode('utf-8')).hexdigest()
        size=(int(digest, 16))%1000000
        return 'https://images.evetech.net/characters/95'+str(size)+'/portrait'

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('mbluser.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return Mbluser.query.get(int(id))