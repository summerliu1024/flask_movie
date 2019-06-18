from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.admin import admin
from app.home import home

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/flask_movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["DEBUG"] = True

db = SQLAlchemy(app)
app.register_blueprint(admin)
app.register_blueprint(home)
