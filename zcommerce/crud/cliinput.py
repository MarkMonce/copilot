with Session(engine) as session:
    
    neworder = Order(order_date="2022-05-01 12:00:00", quantity=1, customer_id=15, product_id=41)
    #

    os.system('clear')
    # print(f"Product ordered:  {product[1]}  Current stock: {product[0]}") 
    product_instance = session.query(Product).get(neworder.product_id)
    customer_instance = session.query(Customer).get(neworder.customer_id)
    neworder.total = neworder.order_total(neworder.quantity, product_instance.price)
   
   

    print('##############################################\n\n')
    print(f'Product ordered: {product_instance.name}\n')
    print(f'Stock before order:  {product_instance.stockqty}\n'
          f'Price: {product_instance.price}\n'
          f'Total Order: {neworder.total}\n')
    print('                    -------\n')
    print(f'Customer: {customer_instance.firstname} {customer_instance.lastname}\n')
    print(f'Account Balance:  {customer_instance.balance}\n')
    print('##############################################\n\n')


    if not (customer_instance.checkbalance(neworder.total) and product_instance.checkstock(neworder.quantity)):
        if not customer_instance.checkbalance(neworder.total):
            print('Account balance is insufficient for order')
        if not product_instance.checkstock(neworder.quantity):
            print('Stock is insufficient for order')
        print('\n=================================Order not processed=================================')
    else:
        customer_instance.updatebalance(neworder.total)
        product_instance.updatestock(neworder.quantity)
        session.add(neworder)

        print('ORDER PROCESSED SUCCESSFULLY ....................\n\n')

        session.commit()

    print('\n\n#####################              POST ORDER STATUS       #########################\n\n')
    print(f'Product ordered: {product_instance.name}\n')
    print(f'Stock after order:  {product_instance.stockqty}\n'
        f'Price: {product_instance.price}\n'
        f'Total Order: {neworder.total}')
    print('--------------\n')
    print(f'Customer: {customer_instance.firstname} {customer_instance.lastname}\n')
    print(f'Remaining  Account Balance:  {customer_instance.balance}\n')
    print('##############################################\n\n')

    #reset stock for product_id to 100
    # product_instance.stockqty = 100
    # session.commit()

    #Update cusomter_id 1 balance to 10000
    # customer_instance.balance = 10000
    # session.commit()