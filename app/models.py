from sqlalchemy.orm import relationship

from app import db, app
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50),nullable=False,unique=True)
    # Tạo mối liên hệ giữa cate và pro, trong lớp Pro tự động thêm trường ref'category', và trường này là obj của cate luôn
    products = relationship('Product', backref='category', lazy=True)
#    lazy=True là khi mình gọi pro nó mới thực hiện

    def __str__(self):
        return self.name
class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
#     khóa ngoại
    category_id =  Column(Integer, ForeignKey(Category.id), nullable=False)
    def __str__(self):
        return self.name
if __name__ == '__main__':

    with app.app_context():
        # c1 = Category(name='Mobile')
        # # truyền obj vào database
        # c2 = Category(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        # db.create_all()
        p1 = Product(name='Iphone 13', price=15000000, category_id=1,
                     image='https://synnexfpt.com/wp-content/uploads/2022/07/Apple-iPhone-13-mini-2.jpg')
        p2 = Product(name='Iphone 13 Pro', price=18000000, category_id=1,
                     image='https://synnexfpt.com/wp-content/uploads/2022/07/Apple-iPhone-13-mini-2.jpg')
        p3 = Product(name='Iphone 14', price=18000000, category_id=1,
                     image='https://synnexfpt.com/wp-content/uploads/2022/07/Apple-iPhone-13-mini-2.jpg')
        p4 = Product(name='Iphone 14 Pro', price=2000000, category_id=1,
                     image='https://synnexfpt.com/wp-content/uploads/2022/07/Apple-iPhone-13-mini-2.jpg')
        p5 = Product(name='Iphone 15', price=2200000, category_id=1,
                     image='https://synnexfpt.com/wp-content/uploads/2022/07/Apple-iPhone-13-mini-2.jpg')
        db.session.add_all([p1,p2,p3,p4,p5])
        db.session.commit()