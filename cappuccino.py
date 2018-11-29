import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def cap_hello(message):
    bot.send_message(message.chat.id, "Давайте приготовим капучино!")
    bot.send_message(message.chat.id, "Инвентарь:\n- Кофемолка. (Лучше всего подойдет "
                                      "ручная. Также можно использовать заранее "
                                      "перемолотый кофе.\n- Турка.\n- Сито или марля.\n"
                                      "- Миксер или взбиватель для молока\n"
                                      "- Приборы для кофепития.\n")
    bot.send_message(message.chat.id, "Необходимые ингредиенты:\n"
                                      "- 1-1.5 чайные ложки зернового или молотого кофе.\n"
                                      "- 50мл молока или сливок.\n"
                                      "- Сахар / ванилин/ ванильный сахар (по вкусу)'")
    """bot.send_message(message.chat.id, "")"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Дальше!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Продолжаем?", reply_markup=keyboard)

def cap_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:")
    bot.send_message(message.chat.id, "Завариваем кофе в турке. Доводим до кипения "
                                      "(когда начнет подниматься кофейная «шапка»)"
                                      "и снимаем с огня. Повторяем процедуру 6-7 раз.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Farther - англ.!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)

def cap_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, "Нагреваем молоко в ёмкости (можно в турке) "
                                      "на медленном огне, по желанию добавляем "
                                      "ванилин и либо сразу, либо после закипания "
                                      "начинаем взбивать молоко взбиателем или "
                                      "миксером до появления мелких пузырьков.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Dalej - пол.!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def cap_step3(message):
    bot.send_message(message.chat.id, "Третий шаг:")
    bot.send_message(message.chat.id, "Нагреваем кружку (обдаем кипятком и вытираем).")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Следваща - болг.!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def cap_step4(message):
    bot.send_message(message.chat.id, "Четвертый шаг:")
    bot.send_message(message.chat.id, "Процеженный кофе наливаем на ¾ чашки, "
                                      "при желании добавляем сахар или другой "
                                      "подсластитель")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Далей - белор.!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def cap_step5(message):
    bot.send_message(message.chat.id, "Пятый шаг:")
    bot.send_message(message.chat.id, "Выливаем молоко в кружку с кофе и ложкой "
                                      "выкладываем пену.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Следеће - серб.!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def cap_step6(message):
    bot.send_message(message.chat.id, "Напиток готов. Приятного аппетита!")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
