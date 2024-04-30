from models.UserModel import UserModel
from repos.RaitingRepository import get_all_raitings_by_distance,get_all_raitings_by_speed
from repos.UserRepository import get_or_create_user

MEDALS = {
    1: "🥇 1 место:",
    2: "🥈 2 место:",
    3: "🥉 3 место:"
}
def get_all_results(message_chat):
    message = "Результаты:\n\n"
    message += "Скорость:\n"
    raitings = get_all_raitings_by_speed()
    for place, raiting in enumerate(raitings,1):
        message += f"{MEDALS.get(place, '')} {raiting.user_id.user_name}: {round(raiting.max_speed, 2)} км\ч\n"
    message += "\n\nДистанция:\n"
    raitings = get_all_raitings_by_distance()
    for place, raiting in enumerate(raitings,1):
        message += f"{MEDALS.get(place, '')} {raiting.user_id.user_name}: {round(raiting.distance, 2)} км\n"
        message += f"Всего: {round(raiting.sum_distance, 2)} км\n"
    return message
def get_results_for_user(message_chat):
    user = get_or_create_user(message_chat.from_user.id, message_chat.from_user.first_name)
    message = "Результаты:\n\n"
    message += "Скорость:\n"
    raitings = get_all_raitings_by_speed()
    for place, raiting in enumerate(raitings,1):
        if raiting.user_id.user_id == user.user_id:
            message += f"{MEDALS.get(place,'')} {raiting.user_id.user_name}: {round(raiting.max_speed, 2)} км\ч\n"
    message += "\n\nДистанция:\n"
    raitings = get_all_raitings_by_distance()
    for place, raiting in enumerate(raitings,1):
        if raiting.user_id.user_id == user.user_id:
            message += f"{MEDALS.get(place,'')} {raiting.user_id.user_name}: {round(raiting.distance, 2)} км\n"
            message += f"Всего: {round(raiting.sum_distance, 2)} км\n"
    return message
