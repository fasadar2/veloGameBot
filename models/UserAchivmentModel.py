from peewee import  AutoField,  ForeignKeyField
from models.BaseModel import *
from models.UserModel import UserModel
from models.AchievementModel import AchievementModel

class UserAchievement(BaseModel):
    user_achievement_id = AutoField(primary_key=True, column_name='user_achievement_id')
    user_id = ForeignKeyField(UserModel, column_name='user_id')
    achievement_id = ForeignKeyField(AchievementModel, column_name='achievement_id')

    class Meta:
        table_name = "user_achievement"