from models.ResultsModel import ResultsModel, UserModel
from repos.RaitingRepository import *

medals = {
    1:"🥇 1 место:",
    2:"🥈 2 место:",
    3:"🥉 3 место:"
}

def save_results(user: UserModel, max_speed, distance):
    try:
        result = ResultsModel()
        result.user_id = user
        result.max_speed = max_speed
        result.distance = distance
        result.save()
        raiting = get_raiting_by_user(user)
        if raiting is not None:
            raiting.distance = result.distance if result.distance > raiting.distance else raiting.distance
            raiting.max_speed = result.max_speed if result.max_speed > raiting.max_speed else raiting.max_speed
            raiting.save()
        return result
    except Exception as e:
        return None

def get_all_results():
    message = "Результаты:\n\n"
    message += "Скорость:\n"
    raitings = get_all_raitings_by_speed()
    for place,raiting in enumerate(raitings):
        message+=f"{medals[place+1]} {raiting.user_id.user_name}: {round(raiting.max_speed, 2)} км\ч\n"
    message+="\n\nДистанция:\n"
    for place,raiting in enumerate(raitings):
        message += f"{medals[place + 1]} {raiting.user_id.user_name}: {round(raiting.distance, 2)} км\n"
    return message
def get_results_for_user(user:UserModel):
    message = "Результаты:\n\n"
    message += "Скорость:\n"
    raitings = get_all_raitings_by_speed()
    for place, raiting in enumerate(raitings):
        if raiting.user_id.user_id == user.user_id:
            message+=f"{medals[place+1]} {raiting.user_id.user_name}: {round(raiting.max_speed, 2)} км\ч\n"
    message += "\n\nДистанция:\n"
    for place, raiting in enumerate(raitings):
        if raiting.user_id.user_id == user.user_id:
            message += f"{medals[place + 1]} {raiting.user_id.user_name}: {round(raiting.distance, 2)} км\n"
    return message