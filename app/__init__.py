from urllib.parse import quote
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'uijdbjgbgbvdj sn fuvndkbi'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saleapp?charset=utf8mb4" % quote("Admin@123")
# ánh xạ database của mysql với pass Admin@123 và bảng saleapp
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app=app)