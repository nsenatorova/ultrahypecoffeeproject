import config
from text import burning_hello_1, burning_hello_ing, burning_hello_inv, burning_step_1, burning_step_3
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def burning_hello(message):
    bot.send_message(message.chat.id, "Давайте приготовим «горящий» кофе!")
    bot.send_message(message.chat.id, burning_hello_1)
    bot.send_message(message.chat.id, burning_hello_inv)
    bot.send_message(message.chat.id, burning_hello_ing)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Конечно!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def burning_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:")
    bot.send_message(message.chat.id, burning_step_1)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Of course - англ.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def burning_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, "Разливаем настоявшийся кофе по ёмкостям.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Samozřejmě - чеш.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def burning_step3(message):
    bot.send_message(message.chat.id, "Третий шаг:")
    bot.send_message(message.chat.id, burning_step_3)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Por supuesto - исп.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def burning_step4(message):
    bot.send_message(message.chat.id, "«Горящий» кофе готов. Приятного кофепития!")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
