from telebot.types import  KeyboardButton, ReplyKeyboardMarkup
def create_replay_keyboard_button_markup(row_width=1,resize_keyboard=True,*buttons_content)->ReplyKeyboardMarkup:
    if len(buttons_content) == 0:
        raise Exception("Empty buttons")
    markup = ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)
    for button_content in buttons_content:
        markup.add(KeyboardButton(button_content))
    return markup