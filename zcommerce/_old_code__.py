    # for i in range (100):
    #     # Create 100 new customer
    #     new_customers = Customer(
    #         firstname=fakedata.first_name(),
    #         lastname=fakedata.last_name(),
    #         address1=fakedata.street_address(),
    #         city=fakedata.city(),
    #         state=fakedata.state_abbr(),
    #         zip=fakedata.zipcode(),
    #         country="USA",
    #         phone=fakedata.phone_number(),
    #         email= fakedata.email())
    #     session.add(new_customers)
    
    # products_list = ['Laptop', 'Desktop', 'Tablet', 'Smartphone', 'Smartwatch', 'Headphones', 'Earbuds', 'Monitor', 'Keyboard', 'Mouse',
    #                      'Printer', 'Scanner', 'Projector', 'Camera', 'Drone', 'Gaming Console', 'Game', 'Router', 'Modem', 'NAS', 'External Hard Drive',
    #                      'Flash Drive', 'Memory Card', 'Battery Pack', 'Charger', 'Cable', 'Adapter', 'Dock', 'Case', 'Cover', 'Screen Protector',]

    # for i in range (30):
    #     new_products = Product(
    #         name=products_list[i],
    #         description=fakedata.sentence(),
    #         price=fakedata.random_int(5, 1500, 5),
    #         stockqty=fakedata.random_int(1, 50, 1)
    #         )
    #     session.add(new_products)
    # Create 50 random orders
    # for i in range(50):
    #     new_orders = Order(
    #         order_date=fakedata.date_time_this_year(),
    #         quantity=fakedata.random_int(1, 10, 1),
    #         total=fakedata.random_int(100, 500, 100),
    #         customer_id=fakedata.random_int(1, 100, 1),
    #         product_id=fakedata.random_int(1, 30, 1)
    #     )
    #     session.add(new_orders)

    # Delete from products all ids less than 27
    # session.query(Product).filter(Product.id < 27).delete()
    #subtract .01 from the price of all products
    # session.query(Product).update({Product.price: Product.price - .01})
    #get a count of customers in each state, sorted in descending order
    # result = session.query(Customer.state, func.count(Customer.id)).group_by(Customer.state).order_by(func.count(Customer.state).desc()).all()
    #clear the terminal

query = select(Product.stockqty, Product.name).where(Product.id == neworder.product_id)
    productordered = session.execute(query).fetchone()
   
   
    query = select(Customer.firstname, Customer.lastname, Customer.balance).where(Customer.id == neworder.customer_id)
    customerorder = session.execute(query).fetchone()
    
    session.commit()

    os.system('clear')
    print(f'Product ID: {neworder.product_id}\n')
    print (f'Customer: {customerorder}\n')
    print(f'Product:{productordered}')
    print(f'Stock Quantity: {productordered[0]}\n')
    print(f'Order Total: {neworder.total}\n')
    if neworder.quantity <= productordered[0]:
        print("Stock is sufficient\n")
    else:
        print("Stock is insufficient\n")

    if neworder.total <= customerorder[2]:
        print("Customer has sufficient funds\n")
    else:
        print('Customer has INSUFFICIENT funds\n')    
        
    #query the product table to get the stock quantity of the product
    # productintock = session.query(Product).filter(Product.id == neworder.product_id).first()
    
   

    
    # sufficient = neworder.product.checkstock(neworder.quantity)

    # if sufficient:
    #     print("Stock is sufficient")
    # print(result)
    # session.commit()