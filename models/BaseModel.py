from peewee import PostgresqlDatabase, Model
import os

# region Для докера
dbUsername = os.environ['POSTGRES_USER']
dbPassword = os.environ['POSTGRES_PASSWORD']
dbName = os.environ['POSTGRES_DB']
host = 'postgres'
# endregion
# dbUsername = "postgres"
# dbPassword = "1"
# dbName = "postgres"
# host = "localhost"
db = PostgresqlDatabase(dbName, host=host, port=5432, user=dbUsername, password=dbPassword)


class BaseModel(Model):
    class Meta:
        database = db  # соединение с базой, из шаблона выше
