from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, Session
from faker import Faker
from sqlalchemy import func, select, text
import os



class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    address1: Mapped[str] = mapped_column(String(100))
    address2: Mapped[Optional[str]] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(50))
    state: Mapped[str] = mapped_column(String(2))
    zip: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(50))
    phone: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(50))
    balance: Mapped[float] = mapped_column()

    order: Mapped[List["Order"]] = relationship("Order", back_populates="customer")

    def updatebalance(self, transaction):
        self.balance -= transaction
        return self.balance
    
    def checkbalance(self, total):
        if self.balance >= total:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.firstname!r}, fullname={self.lastname!r})"

  
    
class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column()
    stockqty: Mapped[int] = mapped_column()

    # Define the relationship to the orders table
    order: Mapped[List["Order"]] = relationship("Order", back_populates="product")
    
    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, price={self.price!r})"
    
    #function to update price of product
    def updateprice(self, newprice):
        self.price = newprice
        return self.price
    
    # #function to deduct stock quantity of product by the amount sold in an order
    def updatestock(self, qty):

        self.stockqty -= qty
        return self.stockqty

    # #determine if product stock is sufficient for order
    def checkstock(self, qty):
        if self.stockqty >= qty:
            return True
        else:
            return False
        
    
class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int] = mapped_column()
    total: Mapped[float] = mapped_column()

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped[Customer] = relationship("Customer", back_populates="order")
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped[Product] = relationship("Product", back_populates="order")

    def __repr__(self) -> str:
        return f"Order(id={self.id!r}, order_date={self.order_date!r})"
    
    def convertorderdate(self):
        splitdate = self.order_date.split(" ")
        extractmonth = splitdate[1]
        extractday = splitdate[2]
        # extracttime = splitdate[3]
        extractyear = splitdate[5]

        date = extractmonth + " " + extractday + " " + extractyear
        return date
    def order_total(self, qty, price):
        total = qty * price
        return total
    

from sqlalchemy import create_engine
engine = create_engine("sqlite:///copilot.db")
Base.metadata.create_all(engine)
fakedata = Faker() 

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
    
