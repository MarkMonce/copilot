from typing import List, Optional
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

    # Define the relationship to the orders table
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="customer")

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
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="product")
    
    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, price={self.price!r})"

class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int] = mapped_column()
    total: Mapped[float] = mapped_column()

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped[Customer] = relationship("Customer", back_populates="orders")
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped[Product] = relationship("Product", back_populates="orders")

    def __repr__(self) -> str:
        return f"Order(id={self.id!r}, order_date={self.order_date!r}, total={self.total!r})"
