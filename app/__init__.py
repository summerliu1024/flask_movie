from flask import Flask

from app.admin import admin
from app.home import home

app = Flask(__name__)

app.register_blueprint(admin)
app.register_blueprint(home)
