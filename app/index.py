from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user


@app.route("/")
def index():
    cate_id = request.args.get('cate_id')
    page = request.args.get()
    kw = request.args.get('kw')
    cats = dao.get_categories()
    pros = dao.get_products_moblie(kw, cate_id)
    return render_template('index.html', categories=cats, products=pros)


@app.route("/admin/login", methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = dao.auth_user(username, password)
    if user:
        login_user(user)  # để lưu user vào trong section duy trì đăng nhập trong trang web --> current name hiện trên trang admin

    return redirect("/admin")


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
