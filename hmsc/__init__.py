from flask_login import LoginManager
import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 判断所处平台
WIN = sys.platform.startswith('win')
if WIN:
    # windows 平台
    prefix = 'sqlite:///'
else:
    # mac or linux 平台
    prefix = 'sqlite:////'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),os.getenv("DATABASE_FILE", 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
db = SQLAlchemy(app)

from hmsc import views, models, commands