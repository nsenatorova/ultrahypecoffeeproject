import config
from text import cap_hello_ing, cap_hello_inv, cap_step_1, cap_step_2, cap_step_4, cap_step_5
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def cap_hello(message):
    bot.send_message(message.chat.id, "Давайте приготовим капучино!")
    bot.send_message(message.chat.id, cap_hello_inv)
    bot.send_message(message.chat.id, cap_hello_ing)
    """bot.send_message(message.chat.id, "")"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Дальше!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Продолжаем??", reply_markup=keyboard)


def cap_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:")
    bot.send_message(message.chat.id, cap_step_1)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Farther - англ.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Продолжаем??", reply_markup=keyboard)


def cap_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, cap_step_2)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Dalej - пол.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Продолжаем??", reply_markup=keyboard)


def cap_step3(message):
    bot.send_message(message.chat.id, "Третий шаг:")
    bot.send_message(message.chat.id, "Нагреваем кружку (обдаем кипятком и вытираем).")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Следваща - болг.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Продолжаем??", reply_markup=keyboard)


def cap_step4(message):
    bot.send_message(message.chat.id, "Четвертый шаг:")
    bot.send_message(message.chat.id, cap_step_4)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Далей - белор.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Продолжаем??", reply_markup=keyboard)


def cap_step5(message):
    bot.send_message(message.chat.id, "Пятый шаг:")
    bot.send_message(message.chat.id, cap_step_5)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Следеће - серб.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Продолжаем??", reply_markup=keyboard)


def cap_step6(message):
    bot.send_message(message.chat.id, "Напиток внезпно оказался готов. Приятного аппетита!")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
