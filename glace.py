import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


def glace(message):
    bot.send_message(message.chat.id, "Давайте приготовим кофе-глясе!")
    bot.send_message(message.chat.id, "Необходимые ингредиенты (на 1 порцию):\n"
                                      "- 3 чайные ложки молотого кофе"
                                      "- 1/2 чайной ложки какао"
                                      "- 1 яичный желток"
                                      "- 50 грамм ванильного мороженого")
    bot.send_message(message.chat.id, "Энергетическая ценность (на 1 порцию):\n"
                                      "Белки: 7.3 грамм\nЖиры: 13.5 грамм"
                                      "Углеводы: 28.2 грамма"
                                      "Калорийность: 264 ккал")
    """bot.send_message(message.chat.id, "")"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Готов продолжить!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def glace_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:")
    bot.send_message(message.chat.id, "Засыпьте в турку кофе, какао и ложку сахара "
                                      "(по вкусу; он необходим для появления корочки "
                                      "(пенки), которая обеспечит напитку более "
                                      "насыщенный вкус и аромат).")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Конечно!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)

def glace_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, "Залейте смесь 150 мл холодной воды. "
                                      "Поставьте турку на слабый огонь.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Да!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def glace_step3(message):
    bot.send_message(message.chat.id, "Третий шаг:")
    bot.send_message(message.chat.id, "Пока турка нагревается, нужно отделить желток "
                                      "и тщательно растереть с чайной ложкой сахара.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Всегда готов!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def glace_step4(message):
    bot.send_message(message.chat.id, "Четвертый шаг:")
    bot.send_message(message.chat.id, "Когда кофе начнёт кипеть, снимите турку с огня"
                                      " и через полминуты снова поставьте на огонь."
                                      "Сделайте так 3 раза.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Ага!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def glace_step5(message):
    bot.send_message(message.chat.id, "Пятый шаг:")
    bot.send_message(message.chat.id, "В яично-сахарную смесь аккуратно влейте через"
                                      " сито сваренный кофе, постоянно помешивая,"
                                      " чтобы желток не схватился.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Еще бы!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

def glace_step6(message):
    bot.send_message(message.chat.id, "Шестой шаг:")
    bot.send_message(message.chat.id, "Перелейте напиток в бокал, положив сверху"
                                      " шарик ванильного мороженого. "
                                      "При желании можно слегка присыпать корицей,"
                                      " шоколадной крошкой или какао."
                                      "Сазу подавать. \nПриятного аппетита!")
    bot.send_message(message.chat.id, "** Можно импровизировать с приправами — перед"
                                      " варкой добавить к кофе немного молотого имбиря,"
                                      " корицы или ванильного сахара (а для яркости вкуса "
                                      "даже чуточку красного перца). Для вечернего варианта "
                                      "при подаче можно добавить чуточку ликера, коньяка или"
                                      "виски. А также развлекайтесь с карамельными или "
                                      "шоколадными соусами поверх мороженого — тут может "
                                      "исполниться любая мечта). Но и без этого по базовому "
                                      "рецепту напиток получается очень насыщенным!")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
