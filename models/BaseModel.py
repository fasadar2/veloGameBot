from peewee import  Model
from db_config import db
import os




class BaseModel(Model):
    class Meta:
        database = db  # соединение с базой, из шаблона выше
