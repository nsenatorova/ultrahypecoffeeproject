def step(message):
    bot.send_message(message.chat.id, " шаг:")
    bot.send_message(message.chat.id, ""
                     ""
                     ""
                     ""
                     ""
                     ""
                     "")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_ready = types.KeyboardButton(text="Готов продолжить!")
    keyboard.add(button_ready)
    bot.send_message(message.chat.id, "Готовы продолжить?", reply_markup=keyboard)

@bot.message_handler(regexp="Готов продолжить!")
def step(message):
    pass
