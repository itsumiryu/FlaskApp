# Flask_App/__init__.py
from flask import Flask

app = Flask(__name__)
app.config.from_object('Flask_App.config')
# flask_blog内にあるconfig.pyの内容をconfigとして扱う

import Flask_App.views
