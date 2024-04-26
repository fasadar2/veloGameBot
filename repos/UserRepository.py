from models.UserModel import UserModel


def get_or_create_user(user_id, user_name) -> UserModel:
    try:
        user_model = UserModel.select().where(UserModel.user_id == user_id).get()
    except Exception as e:
            user_model = UserModel().create(user_id=user_id, user_name=user_name)
    return user_model

