from telebot import types


def get_orar (message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("orar de pe pagina oficiala", url="https://fcim.utm.md/procesul-de-studii/orar/"))