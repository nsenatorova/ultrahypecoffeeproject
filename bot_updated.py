# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

from espresso import esp_hello, esp_step1, esp_step2, esp_step3
from espresso import  esp_step4, esp_step5, esp_step6

from glace import glace_hello, glace_step1, glace_step2, glace_step3
from glace import glace_step4, glace_step5, glace_step6

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def starter(message):
    bot.send_message(message.chat.id, "Привет!\n"
                                      "Я суперкрутой бот, который поможет "
                                      "тебе приготовить самый вкусный кофе в "
                                      "любое время дня и ночи!") # ТУТ ДОЛЖО БЫТЬ ПРИВЕТСВИЕ
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_choice = types.KeyboardButton(text="Выбрать напиток")
    keyboard.add(button_choice)
    bot.send_message(message.chat.id, "Выбирай любой напиток ;)", reply_markup=keyboard)

@bot.message_handler(regexp="Выбрать напиток")
def choice(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_espresso = types.KeyboardButton(text="Эспрессо")
    button_capuchino = types.KeyboardButton(text="Капучино")
    button_glace = types.KeyboardButton(text="Глясе")
    keyboard.add(button_espresso, button_capuchino, button_glace)
    bot.send_message(message.chat.id, "Смотри, чему я могу тебя научить:", reply_markup=keyboard)

@bot.message_handler(regexp="Эспрессо")
def ekspresso(message):
    esp_hello(message)
    @bot.message_handler(regexp="Продолжаем!")
    def eksp1(message):
        esp_step1(message)
    @bot.message_handler(regexp="Конечно!")
    def eksp2(message):
        esp_step2(message)
    @bot.message_handler(regexp="Да!")
    def eksp3(message):
        esp_step3(message)
    @bot.message_handler(regexp="Всегда готов!")
    def eksp4(message):
        esp_step4(message)
    @bot.message_handler(regexp="Ага!")
    def eksp5(message):
        esp_step5(message)
    @bot.message_handler(regexp="Еще бы!")
    def eksp6(message):
        esp_step6(message)

@bot.message_handler(regexp="Капучино")
def cappuccino(message):
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
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Да!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Да!")
    def cap_step1(message):
        bot.send_message(message.chat.id, "Первый шаг")
        bot.send_message(message.chat.id, "Завариваем кофе в турке. Доводим до кипения "
                                          "(когда начнет подниматься кофейная «шапка»)"
                                          "и снимаем с огня. Повторяем процедуру 6-7 раз.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Конечно!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Конечно!")
    def cap_step2(message):
        bot.send_message(message.chat.id, "Второй шаг")
        bot.send_message(message.chat.id, "Нагреваем молоко в ёмкости (можно в турке) "
                                          "на медленном огне, по желанию добавляем "
                                          "ванилин и либо сразу, либо после закипания "
                                          "начинаем взбивать молоко взбиателем или "
                                          "миксером до появления мелких пузырьков.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Ага!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Ага!")
    def cap_step3(message):
        bot.send_message(message.chat.id, "Третий шаг")
        bot.send_message(message.chat.id, "Нагреваем кружку (обдаем кипятком и вытираем).")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Всегда готов!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Всегда готов!")
    def cap_step4(message):
        bot.send_message(message.chat.id, "Четвертый шаг")
        bot.send_message(message.chat.id, "Процеженный кофе наливаем на ¾ чашки, "
                                          "при желании добавляем сахар или другой "
                                          "подсластитель")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Несомненно!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Несомненно!")
    def cap_step5(message):
        bot.send_message(message.chat.id, "Пятый шаг")
        bot.send_message(message.chat.id, "Выливаем молоко в кружку с кофе и ложкой "
                                          "выкладываем пену.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Без сомнений!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Без сомнений!")
    def cap_step6(message):
        bot.send_message(message.chat.id, "Напиток готов. Приятного аппетита!")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Завершить работу.")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)

@bot.message_handler(regexp="Глясе")
def glace(message):
    glace_hello(message)
@bot.message_handler(regexp="Готов!")
def glace1(message):
    glace_step1(message)
@bot.message_handler(regexp="Ready - англ.!")
def glace2(message):
    glace_step2(message)
@bot.message_handler(regexp="Klar - норв.!")
def glace3(message):
    glace_step3(message)
@bot.message_handler(regexp="Valmis - эст.!")
def glace4(message):
    glace_step4(message)
@bot.message_handler(regexp="Redo - швед.!")
def glace5(message):
    glace_step5(message)
@bot.message_handler(regexp="Gata - рум.!")
def glace6(message):
    glace_step6(message)

@bot.message_handler(regexp="Завершить работу.")
def end(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_start = types.KeyboardButton(text="В начало")
    button_end = types.KeyboardButton(text="Остановить бота")
    keyboard.add(button_start, button_end)
    bot.send_message(message.chat.id, "Хотите вернуться в начало или остановить бота?", reply_markup=keyboard)

@bot.message_handler(regexp="В начало")
def to_the_begining(message):
    starter(message)

@bot.message_handler(regexp="Остановить бота")
def stop_bot(message):
    pass
# НАДО ПРИДУМАТЬ, КАК ЗАКАНЧИВАТЬ РАБОТУ БОТА


if __name__ == '__main__':
     bot.polling(none_stop=True)
