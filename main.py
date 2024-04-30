import telebot
import time
from repos.ResultsRepository import save_results
from repos.UserRepository import *
from methods.get_values import try_parse_to_float_value
from methods.logger_to_file import logger_to_file
from services import create_button_service
from commands import start_commands
from services.results_service import get_all_results, get_results_for_user

time_start = time.time()
bot = telebot.TeleBot("6752533782:AAFz0C-ZwQrZhavc_8_oxcCHuXRIibFFpKY")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'Вас приветствует шайтан бот',
                     reply_markup=create_button_service.create_replay_keyboard_button_markup(2, True,
                                                                                             *start_commands))


def get_speed(message):
    try:
        speed = try_parse_to_float_value(message.text)
        bot.send_message(message.chat.id, "Отлично! Теперь введи дистанцию:")
        bot.register_next_step_handler(message, get_distance, speed)
    except ValueError:
        bot.send_message(message.chat.id, "Жулик, не ломай, а теперь все сначала")
        logger_to_file(message.from_user.first_name + " break speed")


def get_distance(message, speed):
    try:
        distance = try_parse_to_float_value(message.text)
        user = get_or_create_user(message.from_user.id, message.from_user.first_name)
        if user is None:
            raise ConnectionRefusedError
        results = save_results(user, speed, distance)
        bot.send_message(message.chat.id, f"Записал для {results.user_id}, {results.max_speed} {results.distance}")
    except ValueError:
        bot.send_message(message.chat.id, "Жулик, не ломай, а теперь все сначала")
        logger_to_file(message.from_user.first_name + " break distance")
    except ConnectionRefusedError:
        bot.send_message(message.chat.id, "С вами что-то не так, ожидайте машину с надписью 'хлеб' для выяснения")
        logger_to_file(message.from_user.first_name + " break user")


@bot.message_handler(content_types=['text'])
def text_handler(message):
    match message.text:
        case '👀 Записать результат':
            bot.send_message(message.chat.id, f'Ага молдоец, а теперь максимальную скорость введи')
            bot.register_next_step_handler(message, get_speed)
        case '✋Общие результаты':
            message_text = get_all_results(message)
            bot.send_message(message.chat.id, message_text)
        case '👑Мои результаты':
            message_text = get_results_for_user(message)
            bot.send_message(message.chat.id, message_text)
        case '❓ Сколько я работаю без сбоев':
            time_now = time.time()
            message_send = f"{int(time_now - time_start)} секунд"
            bot.send_message(message.chat.id, message_send)
        case _:
            bot.send_message(message.chat.id, f'Ты поехавший ? Я тебя просил {message.text} вводить ?')


if __name__ == '__main__':
    print("Запустил в кота пипиской")
    bot.infinity_polling(none_stop=True)
