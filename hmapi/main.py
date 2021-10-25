from fastapi.params import Depends
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from sqlalchemy.orm import Session
import schemas
import models
import graphene
from resolvers import Query
from mutations import HotelMutations
from passlib.context import CryptContext


from starlette.graphql import GraphQLApp
from db_conf import get_db

app = FastAPI()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query,mutation=HotelMutations)))

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated ='auto')

def verify_password(plain_password,hashed_password):
    return pwd_cxt.verify_password(plain_password,hashed_password)

@app.post('/staff')
def new_staff(request: schemas.StaffCreate,db: Session = Depends(get_db)):
    hashed_password = pwd_cxt.hash(request.password)
    new_staff=models.Staff(staff_id = request.staff_id,name = request.name,is_admin=request.is_admin,login = request.login,password = hashed_password)
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff

@app.post('/customers')
def new_customers(request: schemas.CustomerCreate,db: Session = Depends(get_db)):
    new_customer=models.Customer(cus_id=request.cus_id,name=request.name,email=request.email,phone_number= request.phone_number,birth_date=request.birth_date,staff_id=request.staff_id)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@app.post('/order')
def new_order(request: schemas.OrderCreate,db:Session = Depends(get_db)):
    new_order=models.Order(order_id=request.order_id,order_name= request.order_name,order_description=request.order_description,order_price= request.order_price,staff_id=request.staff_id,cus_id=request.cus_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@app.post('/payment')
def new_payment(request:schemas.PaymentCreate,db:Session =Depends(get_db)):
    new_payment=models.Payment(pay_id=request.pay_id,order_id=request.order_id,cus_id=request.cus_id,amount= request.amount,time=request.time)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

@app.post('/shift')
def new_shift(request:schemas.ShiftCreate,db:Session =Depends(get_db)):
    new_shift=models.Shift(id=request.id,staff_id=request.staff_id,shift_time=request.shift_time,shift_name= request.shift_name)
    db.add(new_shift)
    db.commit()
    db.refresh(new_shift)
    return new_shift

@app.get('/staff')
def view_staff(db:Session =Depends(get_db)):
    all_staff = db.query(models.Staff).all()
    return all_staff

@app.get('/customers')
def view_customers(db:Session = Depends(get_db)):
    all_customers=db.query(models.Customer).all()
    return all_customers

@app.get('/order')
def view_order(db:Session = Depends(get_db)):
    all_order=db.query(models.Order).all()
    return all_order

@app.get('/payment')
def view_payment(db:Session = Depends(get_db)):
    all_payment=db.query(models.Payment).all()
    return all_payment

@app.get('/shift')
def view_shift(db:Session = Depends(get_db)):
    all_shift=db.query(models.Shift).all()
    return all_shift

@app.delete('/payment')
def payment_delete(db:Session = Depends(get_db)):
    pass

@app.delete('/staff')
def staff_delete(db:Session = Depends(get_db)):
    pass

@app.delete('/customer')
def customer_delete(db:Session = Depends(get_db)):
    pass

@app.delete('/order')
def order_delete(db:Session = Depends(get_db)):
    pass

@app.delete('/shift')
def shift_delete(db:Session = Depends(get_db)):
    pass

@app.get('/customer/{id}')
def get_cutomer(id:int,db:Session = Depends(get_db)):
    id_customer = db.query(models.Customer).filter(models.Customer.cus_id == id).first()
    if not id_customer:
        return {
            "error": "customer with id not found"
        }
    return id_customer

@app.get("/staff/{id}")
def get_staff(id:int,db:Session = Depends(get_db)):
    id_staff = db.query(models.Staff).filter(models.Staff.staff_id == id).first()
    if not id_staff:
        return{
            "error":"staff with id not found"
        }
    return id_staff

@app.get("/order/{id}")
def get_staff(id:int,db:Session = Depends(get_db)):
    id_order = db.query(models.Order).filter(models.Order.order_id == id).first()
    if not id_order:
        return{
            "error":"order with id not found"
        }
    return id_order
