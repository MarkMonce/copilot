from flask import render_template, redirect, url_for, flash
from zcommerce import app, db
from zcommerce.models import Customer, Product, Order
from zcommerce.routes.customer import CustomerForm
from zcommerce.routes.product import ProductForm
from zcommerce.routes.order import OrderForm

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/customers')
def customer_list():
    customers = Customer.query.all()
    return render_template('customer_list.html', customers=customers)

@app.route('/products')
def product_list():
    products = Product.query.all()
    return render_template('product_list.html', products=products)

@app.route('/orders')
def order_list():
    orders = Order.query.all()
    return render_template('order_list.html', orders=orders)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(name=form.name.data, email=form.email.data)
        db.session.add(customer)
        db.session.commit()
        flash('Customer added successfully!')
        return redirect(url_for('customer_list'))
    return render_template('customer_form.html', form=form)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, price=form.price.data)
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('product_list'))
    return render_template('product_form.html', form=form)

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    form = OrderForm()
    if form.validate_on_submit():
        order = Order(customer_id=form.customer_id.data, product_id=form.product_id.data, quantity=form.quantity.data)
        db.session.add(order)
        db.session.commit()
        flash('Order added successfully!')
        return redirect(url_for('order_list'))
    return render_template('order_form.html', form=form)
