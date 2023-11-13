from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from app import db, app
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True,
                autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), default="https://vodafone.is/lisalib/getfile.aspx?itemid=f5549a56-2237-11ec-80fc-00505681d681")

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    product = relationship('Products', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Products(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Float, default=0)
    img = Column(String(200),
                 default="https://vodafone.is/lisalib/getfile.aspx?itemid=f5549a56-2237-11ec-80fc-00505681d681")
    active = Column(Boolean, default=True)
    id_category = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib
        u = User(name='Admin', username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()))
        db.session.add(u)
        db.session.commit()
        # a1 = Category(name='Mobile')
        # a2 = Category(name='Tablet')
        # a3 = Category(name='Laptop')
        # a4 = Category(name='Phụ kiện khác')
        # db.session.add(a1)
        # db.session.add(a2)
        # db.session.add(a3)
        # db.session.add(a4)
        #
        #
        # c1 = Products(name='Ipad Pro Max', price=30000000, id_category=2)
        # c2 = Products(name='Xiaomi Tablet', price=25000000, id_category=2)
        # c3 = Products(name='Iphone 13 Pro Max', price=32000000, id_category=1)
        # c4 = Products(name='Iphone 12 Pro Max', price=29000000, id_category=1)
        # c5 = Products(name='Asus Gaming', price=35000000, id_category=3)
        # c6 = Products(name='Logitech Keyboard', price=5000000, id_category=4)
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.add(c4)
        # db.session.add(c5)
        # db.session.add(c6)
        # db.session.commit()

