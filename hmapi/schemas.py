from typing import List, Optional
from pydantic import BaseModel
from datetime import date,datetime
from models import Staff,Customer,Order,Payment,Shift
from graphene_sqlalchemy import SQLAlchemyObjectType


class StaffCreate(BaseModel):
    staff_id : int
    name: str
    is_admin: bool
    login:str
    password: str

    class Config():
        orm_mode = True

class CustomerCreate(BaseModel):
    cus_id :int
    name: str
    email: str
    phone_number: int
    birth_date: date
    staff_id: int

class OrderCreate(BaseModel):
    order_id: int
    order_name:str
    order_description:str
    order_price:float
    staff_id: int
    cus_id:int

class PaymentCreate(BaseModel):
    pay_id: int
    order_id: int
    cus_id:int
    amount:float
    time:date

class ShiftCreate(BaseModel):
    id: int
    staff_id: int
    shift_time:datetime
    shift_name:str

class StaffModel(SQLAlchemyObjectType):
    class Meta:
        model = Staff

class ShiftModel(SQLAlchemyObjectType):
    class Meta:
        model = Shift

class PaymentModel(SQLAlchemyObjectType):
    class Meta:
        model = Payment

class OrderModel(SQLAlchemyObjectType):
    class Meta:
        model = Order

class CustomerModel(SQLAlchemyObjectType):
    class Meta:
        model = Customer

class StaffMutate(BaseModel):
    staff_id : int
    name: str
    is_admin: bool
    login:str
    password: str

