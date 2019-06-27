# Flask_App/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('Flask_App.config')
# Flask_App内にあるconfig.pyの内容をconfigとして扱う

db = SQLAlchemy(app)

from Flask_App.views import views, entries
