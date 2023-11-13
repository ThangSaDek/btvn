from app.model import Category, Products, User


def get_categories():
    return Category.query.all()


def get_products_moblie(kw):
    products = Products.query
    if kw:
        products = products.filter(Products.name.contains(kw))
    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)