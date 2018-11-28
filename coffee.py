import telebot
from telebot import types


token = '651925846:AAFEGuB5AgazCbt2SKBQfZc-bt4yF_kJfTc'
bot = telebot.TeleBot(token)


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
        button_ready = types.KeyboardButton(text="Готов!")
        keyboard.add(button_ready)
        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

        @bot.message_handler(regexp="Готов!")
        def step1(message):
            bot.send_message(message.chat.id, "Первый шаг:\nПеремолите зерна.")
            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            button_ready = types.KeyboardButton(text="Ready (англ. Готов)!")
            keyboard.add(button_ready)
            bot.send_message(message.chat.id, "Готовы?", reply_markup=keyboard)

            @bot.message_handler(regexp="Ready (англ. Готов)!")
            def step2(message):
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
                button_ready = types.KeyboardButton(text="Bereit (нем. Готов)!")
                keyboard.add(button_ready)
                bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

                @bot.message_handler(regexp="Bereit (нем. Готов)!")
                def step3(message):
                    bot.send_message(message.chat.id, "Третий шаг:")
                    bot.send_message(message.chat.id, "После полного прогревания смеси "
                                                      "(определить можно по исходящему от неё жару) "
                                                      "добавьте в неё заранее нагретую до 30-40 градусов воду.")
                    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    button_ready = types.KeyboardButton(text="Klar (норв. Готов)!")
                    keyboard.add(button_ready)
                    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

                    @bot.message_handler(regexp="Klar (норв. Готов)!")
                    def step4(message):
                        bot.send_message(message.chat.id, "Четвертый шаг:")
                        bot.send_message(message.chat.id, "Доведите содержимое турки до кипения и "
                                                          "сразу уберите с огня. Тщательно перемешайте смесь, "
                                                          "чтобы поднявшаяся гуща снова оказалась под водой.\n"
                                                          "Снова поставьте турку на огонь.")
                        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        button_ready = types.KeyboardButton(text="Redo (швед. Готов)!")
                        keyboard.add(button_ready)
                        bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

                        @bot.message_handler(regexp="Redo (швед. Готов)!")
                        def step5(message):
                            bot.send_message(message.chat.id, "Пятый шаг:")
                            bot.send_message(message.chat.id, "После второго закипания уберите турку с огня"
                                                              " и накройте блюдцем на 5-7 минут, чтобы смесь "
                                                              "отстоялась.")
                            keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                            button_ready = types.KeyboardButton(text="Valmis (эст. Готов)!")
                            keyboard.add(button_ready)
                            bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

                            @bot.message_handler(regexp="Valmis (эст. Готов)!")
                            def step6(message):
                                bot.send_message(message.chat.id, "Домашний кофе эспрессо готов. Осталось перелить его"
                                                                  " в кофейную чашку, и можно приступать к "
                                                                  "употреблению.\n"
                                                                  "*При желании в кофе можно добавить корицу, взбитые"
                                                                  "сливки или молоко. Это придаст ему особенный вкус.")
                                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                                button_ready = types.KeyboardButton(text="Завершить работу.")
                                keyboard.add(button_ready)
                                bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
