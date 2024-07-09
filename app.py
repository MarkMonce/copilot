from flask import Flask, render_template, flash, redirect, url_for
# from flask_wtf import FlaskForm
from zcommerce import app

#from wtforms import IntegerField, FloatField,StringField,SubmitField, DateField, DateTimeField, TimeField
#from wtforms.validators import DataRequired, Length



# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
from zcommerce import app

if __name__ == "__main__":

    app.run(debug=True)
