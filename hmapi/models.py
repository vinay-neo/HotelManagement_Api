from typing import Counter
from sqlalchemy import Column, DateTime , Integer, String ,Numeric,Boolean
from sqlalchemy.sql.functions import current_date
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey

from db_conf  import Base

# class Book(Base):
#     __tablename__ = "book"
#     id = Column(Integer,primary_key=True ,index=True)
#     name = Column(String(255),nullable=False)
#     author = Column(String(255),nullable=False)
#     description = Column(String(255),nullable=False)
#     total_copies = Column(Integer,nullable=False)
#     available_copies = Column(Integer,nullable=False)

class Staff(Base):
    __tablename__ = "Staff"

    staff_id = Column(Integer, primary_key=True,index=True)
    name = Column(String(255),nullable=False)
    is_admin = Column(Boolean,nullable=False)
    login = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)



class Customer(Base):
    __tablename__ = "Customers"
    
    cus_id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),nullable=False)
    email = Column(String(255),nullable=False)
    phone_number = Column(String(255),nullable=False)
    birth_date = Column(DateTime(timezone=True),nullable=False)
    staff_id = Column(Integer, ForeignKey(Staff.staff_id),nullable=False)




    
class Order(Base):
    __tablename__ = "Orders"

    order_id = Column(Integer, primary_key=True,index=True)
    order_name = Column(String(255),nullable=False)
    order_description = Column(String(255),nullable=False)
    order_price = Column(Numeric(10,2),nullable=False)
    staff_id = Column(Integer,ForeignKey(Staff.staff_id),nullable=False)
    cus_id= Column(Integer,ForeignKey(Customer.cus_id),nullable=False)

class Payment(Base):
    __tablename__ = "Payments"

    pay_id = Column(Integer, primary_key=True,index=True)
    order_id = Column(Integer, ForeignKey(Order.order_id),nullable=False)
    cus_id= Column(Integer, ForeignKey(Customer.cus_id),nullable=False)
    amount = Column(Numeric(10,2),nullable=False)
    time = Column(DateTime(timezone=True),nullable=False)

class Shift(Base):
    __tablename__ = "Shifts"
    id = Column(Integer, primary_key=True,index=True)
    staff_id = Column(Integer,ForeignKey(Staff.staff_id),nullable=False)
    shift_time = Column(DateTime(timezone=True),nullable=False)
    shift_name = Column(String(255),nullable=False)




