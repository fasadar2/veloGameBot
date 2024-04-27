import json
import datetime


def logger_to_file(message):
    date_error = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    json_object = {"date": date_error, "message": message}
    with open("logs/" + date_error + ".json", "w") as json_file:
        json.dump(json_object, json_file)
