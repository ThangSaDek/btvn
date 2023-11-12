from app.model import Category, Products


def get_categories():
    return Category.query.all()


def get_products_moblie(kw):
    products = Products.query
    if kw:
        products = products.filter(Products.name.contains(kw))
    return products.all()
