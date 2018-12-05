import config
from text import glace_ing, glace_inv, glace_1, glace_step_1, glace_step_2, glace_step_3
from text import glace_step_4, glace_step_5, glace_step_6, glace_end
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def glace_hello(message):
    bot.send_message(message.chat.id, "Давайте приготовим кофе-глясе!")
    bot.send_message(message.chat.id, glace_ing)
    bot.send_message(message.chat.id, glace_inv)
    bot.send_message(message.chat.id, glace_1)
    """bot.send_message(message.chat.id, "")"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Готов!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def glace_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:")
    bot.send_message(message.chat.id, glace_step_1)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Ready - англ.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def glace_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, glace_step_2)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Klar - норв.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def glace_step3(message):
    bot.send_message(message.chat.id, "Третий шаг:")
    bot.send_message(message.chat.id, glace_step_3)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Valmis - эст.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def glace_step4(message):
    bot.send_message(message.chat.id, "Четвертый шаг:")
    bot.send_message(message.chat.id, glace_step_4)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Redo - швед.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def glace_step5(message):
    bot.send_message(message.chat.id, "Пятый шаг:")
    bot.send_message(message.chat.id, glace_step_5)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Gata - рум.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def glace_step6(message):
    bot.send_message(message.chat.id, "Шестой шаг:")
    bot.send_message(message.chat.id, glace_step_6)
    bot.send_message(message.chat.id, glace_end)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
