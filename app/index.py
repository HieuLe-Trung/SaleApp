from flask import render_template, request
from app import app
import dao


@app.route("/")
def index():
    # trong thanh tìm kiếm người dùng nhập vào thì sẽ get được key
    kw = request.args.get("kw")

    cates = dao.get_categories()
    prods = dao.get_products(kw)
    # tạo biến để lấy database, import thư mục chứa data
    return render_template('index.html', categories=cates, products=prods)


if __name__ == '__main__':
    app.run(debug=True)

