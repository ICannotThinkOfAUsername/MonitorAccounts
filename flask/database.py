from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import pa_username, db_password

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=pa_username,
    password=db_password,
    hostname=pa_username+".mysql.pythonanywhere-services.com",
    databasename=pa_username+"$default",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24))
    time = db.Column(db.Integer)
    active = db.Column(db.Boolean)