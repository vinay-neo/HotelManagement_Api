#todo resolovers in graphene

import schemas
import graphene
from db_conf import db
import models

class Query(graphene.ObjectType):
    all_Shifts = graphene.List(schemas.ShiftModel)
    all_Payment = graphene.List(schemas.PaymentModel)
    all_Order = graphene.List(schemas.OrderModel)
    all_Customer = graphene.List(schemas.CustomerModel)
    all_Staff = graphene.List(schemas.StaffModel)

    def resolve_all_Shifts(self,info):
        query = schemas.ShiftModel.get_query(info)
        return query.all()

    def resolve_all_Payment(self,info):
        query = schemas.PaymentModel.get_query(info)
        return query.all()

    def resolve_all_Order(self,info):
        query = schemas.OrderModel.get_query(info)
        return query.all()

    def resolve_all_Customer(self,info):
        query = schemas.CustomerModel.get_query(info)
        return query.all()

    def resolve_all_Staff(self,info):
        query = schemas.StaffModel.get_query(info)
        return query.all()