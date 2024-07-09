from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
#from wtforms import IntegerField, FloatField,StringField,SubmitField, DateField, DateTimeField, TimeField
#from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
