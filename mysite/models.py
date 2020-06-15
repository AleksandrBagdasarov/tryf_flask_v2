from datetime import datetime
from mysite import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id            =  db.Column(db.Integer, primary_key=True)
    first_name    =  db.Column(db.String(20))
    last_name     =  db.Column(db.String(20))
    email         =  db.Column(db.String(50), unique=True, nullable=False)
    img           =  db.Column(db.String(20), nullable=False, default='default_user.jpg')
    password      =  db.Column(db.String(20), nullable=False)
    register_date =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"User('{self.first_name}','{self.last_name}','{self.email}','{self.img}','{self.register_date}'"


class Product(db.Model):
    id            =  db.Column(db.Integer, primary_key=True)
    title         =  db.Column(db.String(20))
    description   =  db.Column(db.String(120))
    img           =  db.relationship('Product_img', backref='product', lazy=True)
    register_date =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"User('{self.id}','{self.title}','{self.description}','{self.img}','{self.register_date}'"



class Product_img(db.Model):
    id            =  db.Column(db.Integer, primary_key=True)
    img           =  db.Column(db.String(20), nullable=False, default='default_product.jpg')
    product_id    =  db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.img}','{self.product_id}'"

    
    