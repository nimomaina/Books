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
    pass

class User(UserMixin, db.Model):
    pass


