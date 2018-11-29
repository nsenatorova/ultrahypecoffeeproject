import config
import telebot
from telebot import types

from espresso import esp_hello, esp_step1, esp_step2, esp_step3
from espresso import esp_step4, esp_step5, esp_step6
from bot import ekspresso

bot = telebot.TeleBot(config.token)


def irish_hello(message):
    bot.send_message(message.chat.id, "Давайте приготовим холодный ирландский кофе!")
    bot.send_message(message.chat.id, "Инвентарь:\n- Чистое сито (марля)\n"
                                      "- Кастрюля с толстым дном")
    bot.send_message(message.chat.id, "Необходимые ингредиенты:\n"
                                      "- 1 стакан черного кофе\n"
                                      "- 1 чайная ложка сахара\n"
                                      "- 1/4 стакана сливой"
                                      "- 2 столовые ложки взбитых сливок"
                                      "- 3 кусочка льда"
                                      "- 60 мл ирландского виски"
                                      "- молотый мускатный орех (по вкусу)")
    bot.send_message(message.chat.id, "Энергетическая ценность (на 1 порцию):\n"
                                      "Белки: 3.9 грамм\nЖиры: 17.4 грамм"
                                      "Углеводы:17.6 грамма"
                                      "Калорийность: 379 ккал")
    """bot.send_message(message.chat.id, "")"""
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Следующий шаг!")
    button_need_espresso = types.KeyboardButton(text="Мне нужен готовый кофе!")
    keyboard.add(button_ready, button_need_espresso)
    bot.send_message(message.chat.id, "Продолжаем?", reply_markup=keyboard)


def irish_step1(message):
    bot.send_message(message.chat.id, "Первый шаг:")
    bot.send_message(message.chat.id, "В миске смешайте горячий кофе, сливки и сахар "
                                      "и перемешивайте, пока сахар не растворится. "
                                      "Слегка охладите Всю смесь довести до кипения "
                                      "и варить еще одну минуту.")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Next step - англ.!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Продолжаем?", reply_markup=keyboard)

def irish_step2(message):
    bot.send_message(message.chat.id, "Второй шаг:")
    bot.send_message(message.chat.id, "В высокий бокал положите 1 столовую ложку "
                                      "взбитых сливок и залейте кофе. Добавьте лед и "
                                      "виски. Сверху украсьте взбитыми сливками и "
                                    "посыпьте мускатным орехом.")
    bot.send_message(message.chat.id, "Холодный ирландский кофе готов. Приятного кофепития!")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Завершить работу.")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Завершить работу?", reply_markup=keyboard)
