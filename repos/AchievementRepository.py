from models.UserAchivmentModel import UserAchievement, AchievementModel, UserModel


def get_achivements_by_user(user: UserModel) -> list[UserAchievement]:
    achievements = UserAchievement.select().where(UserAchievement.user_id == user)
    return achievements


def add_achievement_to_user(user: UserModel, achievement: AchievementModel) -> UserAchievement:
    achievement = UserAchievement.create(user_id=user, achievement_id=achievement)
    return achievement


def get_all_achievements() -> list[AchievementModel]:
    return AchievementModel.select()
