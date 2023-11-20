from app.model import Category, Products, UserRoleEnums
from app import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user
from flask import redirect


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnums.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnums.ADMIN


class AuthenticatedUser2(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyProductView(AuthenticatedAdmin):
    column_list = ['id', 'name', 'price', 'active']
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    can_export = True
    edit_modal = True


class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'product']


class MyStatsView(AuthenticatedUser):
    @expose("/")
    def __index__(self):
        return self.render("admin/stats.html")


class LogoutView(AuthenticatedUser2):
    @expose("/")
    def __index__(self):
        logout_user()
        return redirect('/admin')


admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Products, db.session))
admin.add_view(MyStatsView(name="Thống kê"))
admin.add_view(LogoutView(name="Đăng xuất"))
