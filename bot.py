# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["choice"])
def choice(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_espresso = types.KeyboardButton(text="Эспрессо")
    button_capuchino = types.KeyboardButton(text="Капучино")
    keyboard.add(button_espresso, button_capuchino)
    bot.send_message(message.chat.id, "Какой напиток вы хотите приготовить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Эспрессо")
    def ekspresso(message):
        bot.send_message(message.chat.id, "Давайте приготовим эспрессо!")
        bot.send_message(message.chat.id, "Инвентарь:\n- Кофемолка. (Лучше всего подойдет ручная.")
        bot.send_message(message.chat.id, "Также можно использовать заранее перемолотый кофе.")
        bot.send_message(message.chat.id, "- Турка.\n- Кастрюля.\n- Блюдце.")
        bot.send_message(message.chat.id, "- Приборы для кофепития.")
        bot.send_message(message.chat.id, "Необходимые ингредиенты:")
        bot.send_message(message.chat.id, "- 2-3 ложки зернового или молотого кофе.")
        bot.send_message(message.chat.id, "- 200 миллилитров фильтрованной воды.")
        bot.send_message(message.chat.id, "- 2-3 ложечки сахара.\n- 1/5 чайной ложки соли.")
        """bot.send_message(message.chat.id, "")"""
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Готов продолжить!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)
        @bot.message_handler(regexp="Готов продолжить!")
        def step1(message):
            bot.send_message(message.chat.id, "Первый шаг:\nПеремолите зерна.")
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_ready = types.KeyboardButton(text="Готов продолжить!")
            keyboard.add(button_ready)
            bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)
            @bot.message_handler(regexp="Готов продолжить!")
            def step2(message):
                pass


if __name__ == '__main__':
     bot.polling(none_stop=True)
