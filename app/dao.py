from app.model import Category, Products, User
import hashlib


def get_categories():
    return Category.query.all()


def get_products_moblie(kw, cate_id):
    products = Products.query
    if kw:
        products = products.filter(Products.name.contains(kw))

    if cate_id:
        products = products.filter(Products.id_category.__eq__(cate_id))
    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()
