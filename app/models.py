from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class Book(db.Model):

    '''
    Class blog that hold all blog data
    '''
    __tablename__='books'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    book_pic = db.Column(db.String(),default = 'default.jpg')
    review = db.relationship('Review', backref='blog', lazy='dynamic')


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(), default='default.jpg')
    pass_secure = db.Column(db.String(255))
    book = db.relationship('Book', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_pic_path}')"



class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    description = db.Column(db.Text)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
