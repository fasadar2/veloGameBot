from peewee import AutoField, ForeignKeyField, DecimalField

from models.BaseModel import *
from models.UserModel import UserModel


class ResultsModel(BaseModel):
    result_id = AutoField(primary_key=True,column_name='result_id')
    user_id = ForeignKeyField(UserModel,column_name='user_id')
    max_speed = DecimalField(max_digits=10,column_name='max_speed')
    distance = DecimalField(max_digits=10,column_name='distance')

    class Meta:
        table_name = "results"
