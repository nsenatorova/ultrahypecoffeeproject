# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

from espresso import esp_hello, esp_step1, esp_step2, esp_step3
from espresso import  esp_step4, esp_step5, esp_step6

from cappuccino import cap_hello, cap_step1, cap_step2, cap_step3
from cappuccino import cap_step4, cap_step5, cap_step6

from glace import glace_hello, glace_step1, glace_step2, glace_step3
from glace import glace_step4, glace_step5, glace_step6

# from cold_irish import irish_hello, irish_step2, irish_step1

from starter_hello import starter

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def lets_start(message):
    starter(message)

@bot.message_handler(regexp="Выбрать напиток")
def choice(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_espresso = types.KeyboardButton(text="Эспрессо")
    button_capuchino = types.KeyboardButton(text="Капучино")
    button_glace = types.KeyboardButton(text="Глясе")
    button_cold_irish = types.KeyboardButton(text="Холодный ирландский кофе")
    keyboard.add(button_espresso, button_capuchino, button_glace, button_cold_irish)
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
    cap_hello(message)
    @bot.message_handler(regexp="Дальше!")
    def cap1(message):
        cap_step1(message)
    @bot.message_handler(regexp="Farther - англ.!")
    def cap2(message):
        cap_step2(message)
    @bot.message_handler(regexp="Dalej - пол.!")
    def cap3(message):
        cap_step3(message)
    @bot.message_handler(regexp="Следваща - болг.!")
    def cap4(message):
        cap_step4(message)
    @bot.message_handler(regexp="Далей - белор.!")
    def cap5(message):
        cap_step5(message)
    @bot.message_handler(regexp="Следеће - серб.!")
    def cap6(message):
        cap_step6(message)

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

"""@bot.message_handler(regexp="Холодный ирландский кофе")
def cold_irish(message):
    irish_hello(message)
@bot.message_handler(regexp="Следующий шаг!")
def cold_irish_1(message):
    irish_step1(message)
@bot.message_handler(regexp="Next step - англ.!")
def cold_irish_2(message):
    irish_step2(message)"""


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
