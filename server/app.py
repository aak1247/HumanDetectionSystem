from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__, static_url_path='', static_folder='static/build')
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/human_detection?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from . import main
app.register_blueprint(main)