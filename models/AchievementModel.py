from peewee import CharField, AutoField, TextField
from models.BaseModel import *
class AchievementModel(BaseModel):
    id = AutoField(primary_key=True,column_name="id")
    name = CharField(max_length=200,column_name="name")
    description = TextField(column_name="description")
    class Meta:
        table_name = "achievement"