# import os
# from flask import Flask    #Add these elsewhere: render_template, flash, redirect, url_for
# import sqlalchemy
# from sqlalchemy import create_engine
# #from flask_migrate import Migrate
# from sqlalchemy.ext.declarative import declarative_base

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'

# DeclarativeBase = declarative_base()

# from sqlalchemy import create_engine
# class Base(DeclarativeBase):
#     pass
# engine = create_engine("sqlite:///copilot.db")
# db = Base.metadata.create_all(engine)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from zcommerce import routes


