from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    kw = request.args.get('kw')
    cats = dao.get_categories()
    pros = dao.get_products_moblie(kw)
    return render_template('index.html', categories=cats, products=pros)


if __name__ == '__main__':
    app.run(debug=True)
