from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product
from app import app, db
from flask_admin import Admin,BaseView,expose

admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')

class MyProductView(ModelView):
    can_export = True
    can_edit = True
    form_columns = ['id','name','price']
    column_searchable_list = ['name']
    column_filters = ['name','price']
    column_editable_list = ['name','price']
    edit_modal = True
class MyCategoryView(ModelView):
    column_list = ['name', 'products']

class MyStateView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")
admin.add_view(MyCategoryView(Category,db.session))
admin.add_view(MyProductView(Product,db.session))
admin.add_view(MyStateView(name="Thống kê báo cáo"))