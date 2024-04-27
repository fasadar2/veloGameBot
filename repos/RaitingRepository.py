from models.RatingModel import RaitingModel


def get_raiting_by_user(user) -> RaitingModel:
    try:
        raiting = RaitingModel.select().where(RaitingModel.user_id == user.user_id).get()
    except:
        raiting = RaitingModel.create(user_id=user, max_speed=0.0, distance=0.0)
    return raiting


def get_all_raitings_by_speed() -> list[RaitingModel]:
    return RaitingModel.select().order_by(RaitingModel.max_speed)[::-1]


def get_all_raitings_by_distance() -> list[RaitingModel]:
    return RaitingModel.select().order_by(RaitingModel.distance)[::-1]
