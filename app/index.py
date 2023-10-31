from flask import Flask, render_template, request
import dao

app = Flask(__name__)


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

