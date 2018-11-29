import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def starter(message):
    bot.send_message(message.chat.id, "Привет!\n"
                                      "Я суперкрутой бот, который поможет "
                                      "тебе приготовить самый вкусный кофе в "
                                      "любое время дня и ночи!") # ТУТ ДОЛЖО БЫТЬ ПРИВЕТСВИЕ
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_choice = types.KeyboardButton(text="Выбрать напиток")
    keyboard.add(button_choice)
    bot.send_message(message.chat.id, "Выбирай любой напиток ;)", reply_markup=keyboard)
