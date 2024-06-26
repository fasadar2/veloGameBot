from models.UserModel import UserModel
from models.ResultsModel import ResultsModel
from models.RatingModel import RaitingModel
from db_config import db


def old_but_work():
    print("Starting migration")
    # region Delete tables
    try:
        ResultsModel.drop_table()
    except:
        print("Table not found")
    try:
        RaitingModel.drop_table()
    except:
        print("Table not found")
    try:
        UserModel.drop_table()
    except Exception as e:
        print("Table not found", e)
    # endregion
    # region Create tables
    try:
        UserModel.create_table()
    except:
        print("Table already exists")
    try:
        ResultsModel.create_table()
    except:
        print("Table already exists")
    try:
        RaitingModel.create_table()
    except:
        print("Table already exists")
    # endregion
    print("End migrations")


if __name__ == "__main__":
    old_but_work()
