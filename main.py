import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
import time
from repos.UserRepository import *
from repos.ResultsRepository import *

time_start = time.time()
bot = telebot.TeleBot("6752533782:AAFz0C-ZwQrZhavc_8_oxcCHuXRIibFFpKY")


def start_markup():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton('👀 Записать результат')
    btn2 = KeyboardButton('✋Общие результаты', )
    btn3 = KeyboardButton('👑Мои результаты', )
    btn4 = KeyboardButton('❓ Сколько я работаю без сбоев')
    markup.add(btn1, btn2, btn3,btn4)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Вас приветствует шайтан бот',
                     reply_markup=start_markup())


def get_speed(message):
    try:
        speed = float(message.text)
        bot.send_message(message.chat.id, "Отлично! Теперь введи дистанцию:")
        bot.register_next_step_handler(message, get_distance, speed)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение для скорости. Тепрь все заново, доволен ?")


def get_distance(message, speed):
    try:
        distance = float(message.text)
        user = get_or_create_user(message.from_user.id, message.from_user.first_name)
        if user is None:
            raise ConnectionRefusedError
        results = save_results(user, speed, distance)
        bot.send_message(message.chat.id, f"Записал для {results.user_id}, {results.max_speed} {results.distance}")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение для дистанции. Тепрь все заново, доволен ?")
    except ConnectionRefusedError:
        bot.send_message(message.chat.id, "С вами что-то не так, ожидайте машину с надписью 'хлеб' для выяснения")
@bot.message_handler(content_types=['text'])
def text_handler(message):
    match message.text:
        case '👀 Записать результат':
            bot.send_message(message.chat.id, f'Ага молдоец, а теперь максимальную скорость введи')
            bot.register_next_step_handler(message, get_speed)
        case '✋Общие результаты':
            message_text = get_all_results()
            bot.send_message(message.chat.id,message_text)
        case '👑Мои результаты':
            user = get_or_create_user(message.from_user.id, message.from_user.first_name)
            if user is None:
                raise ConnectionRefusedError
            message_text = get_results_for_user(user)
            bot.send_message(message.chat.id, message_text)
        case '❓ Сколько я работаю без сбоев':
            time_now = time.time()
            bot.send_message(message.chat.id, f"{int(time_now - time_start)} секунд")
        case _:
            bot.send_message(message.chat.id, f'Ты поехавший ? Я тебя просил {message.text} вводить ?')


if __name__ == '__main__':
    print("Запустил в кота пипиской")
    bot.infinity_polling(none_stop=True)
