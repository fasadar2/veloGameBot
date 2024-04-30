from models.ResultsModel import ResultsModel, UserModel
from repos.RaitingRepository import *




def save_results(user: UserModel, max_speed, distance):
    try:
        result = ResultsModel().create(user_id=user,max_speed=max_speed,distance=distance)
        raiting = get_raiting_by_user(user)
        if raiting is not None:
            raiting.distance = result.distance if result.distance > raiting.distance else raiting.distance
            raiting.max_speed = result.max_speed if result.max_speed > raiting.max_speed else raiting.max_speed
            raiting.sum_distance = float(raiting.sum_distance) + result.distance
            raiting.save()
        return result
    except Exception as e:
        return None






