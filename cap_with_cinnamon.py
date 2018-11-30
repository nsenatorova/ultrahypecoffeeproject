import config
from text import with_cinnamon_hello_1, with_cinnamon_hello_ing, with_cinnamon_hello_inv
from text import with_cinnamon_step_1, with_cinnamon_step_3, with_cinnamon_step_4, with_cinnamon_step_5
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def with_cinnamon_hello(message):
    bot.send_message(message.chat.id, "Давайте приготовим капучино с корицей!")
    bot.send_message(message.chat.id, with_cinnamon_hello_1)
    bot.send_message(message.chat.id, with_cinnamon_hello_inv)
    bot.send_message(message.chat.id, with_cinnamon_hello_ing)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Да!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def with_cinnamon_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:")
    bot.send_message(message.chat.id, with_cinnamon_step_1)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Yes - англ.!")
    button_how_to_espresso = types.KeyboardButton(text="Как приготовить эспрессо?")
    keyboard.add(button_ready, button_how_to_espresso)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def with_cinnamon_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, "Посыпьте кофе молотой корицей.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Jā - лат.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def with_cinnamon_step3(message):
    bot.send_message(message.chat.id, "Третий шаг:")
    bot.send_message(message.chat.id, with_cinnamon_step_3)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Tha - шотл.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def with_cinnamon_step4(message):
    bot.send_message(message.chat.id, "Четвертый шаг:")
    bot.send_message(message.chat.id, with_cinnamon_step_4)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="kyllä - фин.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def with_cinnamon_step5(message):
    bot.send_message(message.chat.id, "Пятый шаг:")
    bot.send_message(message.chat.id, with_cinnamon_step_5)
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Jo - люкс.!")
    button_start = types.KeyboardButton(text="В начало")
    keyboard.add(button_ready, button_start)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)


def with_cinnamon_step6(message):
    bot.send_message(message.chat.id, "Напиток готов!")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
