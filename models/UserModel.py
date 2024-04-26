from peewee import CharField
from models.BaseModel import *


class UserModel(BaseModel):
    user_id = CharField(unique=True, primary_key=True, max_length=150,column_name='user_id')
    user_name = CharField(unique=True, max_length=511,column_name='user_name')

    class Meta:
        table_name = 'user'
