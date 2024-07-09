from flask import render_template
from myproject import app, db
from myproject.models import Customer#####Update the root folder and match it up to this "myproject is not the name of the project"

@app.route('/customers')
def customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)
