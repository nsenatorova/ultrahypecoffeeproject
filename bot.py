# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

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
    keyboard.add(button_espresso, button_capuchino)
    bot.send_message(message.chat.id, "Смотри, чему я могу тебя научить:", reply_markup=keyboard)

@bot.message_handler(regexp="Эспрессо")
def ekspresso(message):
    bot.send_message(message.chat.id, "Давайте приготовим эспрессо!")
    bot.send_message(message.chat.id, "Инвентарь:\n- Кофемолка. "
                     "(Лучше всего подойдет ручная."
                     "Также можно использовать заранее перемолотый кофе.\n"
                     "- Турка.\n- Кастрюля.\n- Блюдце.\n"
                     "- Приборы для кофепития.\n")
    bot.send_message(message.chat.id, "Необходимые ингредиенты:\n"
                         "- 2-3 ложки зернового или молотого кофе.\n"
                         "- 200 миллилитров фильтрованной воды.\n"
                         "- 2-3 ложечки сахара.\n- 1/5 чайной ложки соли.")
    """bot.send_message(message.chat.id, "")"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Готов продолжить!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Готов продолжить!")
    def esp_step1(message):
        bot.send_message(message.chat.id, "Первый шаг:\nПеремолите зерна.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Конечно!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)
    @bot.message_handler(regexp="Конечно!")
    def esp_step2(message):
        bot.send_message(message.chat.id, "Второй шаг:")
        bot.send_message(message.chat.id, "Возьмите турку (0.25 мл) "
                                          "и насыпьте в нее 2-3 чайные ложечки молотой смеси, пару "
                                          "ложек сахара и немного крупной поваренной соли.\n"
                                          "Тщательно все перемешайте.\n"
                                          "Поставьте турку на огонь для прогревания."
                                          "Держите турку на расстоянии нескольких сантиметров "
                                          "над огнем и регульрно помешивайте, чтобы сухая смесь не пригорела.\n"
                                          "Начните нагревать воду до 40 градусов.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Да!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Да!")
    def esp_step3(message):
        bot.send_message(message.chat.id, "Третий шаг:")
        bot.send_message(message.chat.id, "После полного прогревания смеси "
                                          "(определить можно по исходящему от неё жару) "
                                          "добавьте в неё заранее нагретую до 30-40 градусов воду.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Всегда готов!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Всегда готов!")
    def esp_step4(message):
        bot.send_message(message.chat.id, "Четвертый шаг:")
        bot.send_message(message.chat.id, "Доведите содержимое турки до кипения и "
                                          "сразу уберите с огня. Тщательно перемешайте смесь, "
                                          "чтобы поднявшаяся гуща снова оказалась под водой.\n"
                                          "Снова поставьте турку на огонь.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Ага!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Ага!")
    def esp_step5(message):
        bot.send_message(message.chat.id, "Пятый шаг:")
        bot.send_message(message.chat.id, "После второго закипания уберите турку с огня"
                                          " и накройте блюдцем на 5-7 минут, чтобы смесь "
                                          "отстоялась.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Еще бы!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)
    @bot.message_handler(regexp="Еще бы!")
    def esp_step6(message):
        bot.send_message(message.chat.id, "Домашний кофе эспрессо готов. Осталось перелить его"
                                          " в кофейную чашку, и можно приступать к "
                                          "употреблению.\n"
                                          "*При желании в кофе можно добавить корицу, взбитые"
                                          "сливки или молоко. Это придаст ему особенный вкус.")
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_ready = types.KeyboardButton(text="Завершить работу.")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)

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
