# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

from espresso import *
from cappuccino import *
from glace import *
from burning_coffee import *
from with_cinnamon import *

# from cold_irish import irish_hello, irish_step2, irish_step1

from starter_hello import starter

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def lets_start(message):
    starter(message)

@bot.message_handler(regexp="Выбрать напиток")
def choice(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_espresso = types.KeyboardButton(text="Эспрессо")
    button_capuchino = types.KeyboardButton(text="Капучино обычный")
    button_glace = types.KeyboardButton(text="Глясе")
    # button_cold_irish = types.KeyboardButton(text="Холодный ирландский кофе")
    # button_with_honey = types.KeyboardButton(text="Кофе с мёдом")
    button_cap_with_cinnamon = types.KeyboardButton(text="Капучино с корицей")
    button_burning = types.KeyboardButton(text="«Горящий» кофе")
    keyboard.add(button_espresso, button_capuchino, button_glace,
                 button_cap_with_cinnamon, button_burning)
    bot.send_message(message.chat.id, "Смотри, чему я могу тебя научить:", reply_markup=keyboard)


@bot.message_handler(regexp="Эспрессо") # Всегда готов, Очень хороший
def ekspresso(message):
    bot.send_message(message.chat.id, "Как приготовить эспрессо?")
    bot.send_audio(message.chat.id, audio=open('music/Оченьхороший.ogg', 'rb'))
    esp_hello(message)
    @bot.message_handler(regexp="Всегда готов!")
    def eksp1(message):
        esp_step1(message)
    @bot.message_handler(regexp="Always ready - англ.!")
    def eksp2(message):
        esp_step2(message)
    @bot.message_handler(regexp="Alltid klar - норв.!")
    def eksp3(message):
        esp_step3(message)
    @bot.message_handler(regexp="Alltid redo - швед.!")
    def eksp4(message):
        esp_step4(message)
    @bot.message_handler(regexp="Aina valmiina - фин.!")
    def eksp5(message):
        esp_step5(message)
    @bot.message_handler(regexp="Altid klar - дат.!")
    def eksp6(message):
        esp_step6(message)

@bot.message_handler(regexp="Капучино обычный") # "Дальше", "Хороший"
def cappuccino(message):
    bot.send_message(message.chat.id, "Как приготовить капучино?")
    bot.send_audio(message.chat.id, audio=open('music/Хороший.ogg', 'rb'))
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

@bot.message_handler(regexp="Глясе") # "Готов", "Замечательный"
def glace(message):
    bot.send_message(message.chat.id, "Как приготовить гляссе?")
    bot.send_audio(message.chat.id, audio=open('music/Замечательный.ogg', 'rb'))
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

@bot.message_handler(regexp="Капучино с корицей") # "Да", "Неплохой"
def cinnamon(message):
    bot.send_message(message.chat.id, "Как приготовить капучино с корицей?")
    bot.send_audio(message.chat.id, audio=open('music/Неплохой.ogg', 'rb'))
    with_cinnamon_hello(message)
    @bot.message_handler(regexp="Да!")
    def cinnamon1(message):
        with_cinnamon_step1(message)
    @bot.message_handler(regexp="Yes - англ.!")
    def cinnamon2(message):
        with_cinnamon_step2(message)
    @bot.message_handler(regexp="Jā - лат.!")
    def cinnamon3(message):
        with_cinnamon_step3(message)
    @bot.message_handler(regexp="Tha - шотл.!")
    def cinnamon4(message):
        with_cinnamon_step4(message)
    @bot.message_handler(regexp="kyllä - фин.!")
    def cinnamon5(message):
        with_cinnamon_step5(message)
    @bot.message_handler(regexp="Jo - люкс.!")
    def cinnamon6(message):
        with_cinnamon_step6(message)

@bot.message_handler(regexp="«Горящий» кофе") # "Конечно", "Прекрасный"
def burning(message):
    bot.send_message(message.chat.id, "Как приготовить «горящий» кофе?")
    bot.send_audio(message.chat.id, audio=open('music/Прекрасный.ogg', 'rb'))
    burning_hello(message)
    @bot.message_handler(regexp="Конечно!")
    def burn1(message):
        burning_step1(message)
    @bot.message_handler(regexp="Of course - англ.!")
    def burn2(message):
        burning_step2(message)
    @bot.message_handler(regexp="Samozřejmě - чеш.!")
    def burn3(message):
        burning_step3(message)
    @bot.message_handler(regexp="Por supuesto - исп.!")
    def burn4(message):
        burning_step4(message)

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
    keyboard.add(button_start)
    bot.send_message(message.chat.id, "Хотите вернуться в начало ?", reply_markup=keyboard)

@bot.message_handler(regexp="В начало")
def to_the_begining(message):
    starter(message)




if __name__ == '__main__':
     bot.polling(none_stop=True)
