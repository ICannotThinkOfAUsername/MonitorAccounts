from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="USERNAME",
    password="PASSWORD",
    hostname="USERNAME.mysql.pythonanywhere-services.com",
    databasename="USERNAME$default",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://acow1:themysqlpassword3@acow1.mysql.pythonanywhere-services.com/acow1$default'
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    time = db.Column(db.Integer)
    active = db.Column(db.Boolean)