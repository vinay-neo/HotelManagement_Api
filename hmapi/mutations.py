import graphene
import models
from db_conf import db
from schemas import StaffMutate
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated ='auto')

class CreateNewStaff(graphene.Mutation):
    class Arguments:
        staff_id = graphene.Int(required=True)
        name = graphene.String(required=True)
        is_admin = graphene.Boolean(required=True)
        login = graphene.String(required=True)

        password = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root , info,staff_id,name,is_admin,login,password):
        hashed_password = pwd_cxt.hash(password)
        staff_ = StaffMutate(staff_id=staff_id,name=name,is_admin=is_admin,login=login,password=hashed_password)
        db_staff = models.Staff(staff_id=staff_.staff_id,name=staff_.name,is_admin=staff_.is_admin,login=staff_.login,password=staff_.password)
        db.add(db_staff)
        db.commit()
        db.refresh(db_staff)
        ok = True
        return CreateNewStaff(ok=ok) 

class HotelMutations(graphene.ObjectType):
    create_new_staff = CreateNewStaff.Field()