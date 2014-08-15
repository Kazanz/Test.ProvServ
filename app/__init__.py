from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
config = config.DevConfig
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)

from app import views, models
