import telebot
import webbrowser

import config as API
import App.Keyboard as Keyboard

bot =telebot.TeleBot(API.API)

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://fcim.utm.md/procesul-de-studii/orar/')
    bot.send_message(message.chat.id, 'Pagina a fost deschisa', reply_markup=Keyboard.get_orar(message))
    
@bot.message_handler(commands=['start', 'hello','Hi'])
def start(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}') 
    
@bot.message_handler(commands=['help', 'ajutor', 'помоги'])
def help_command(message):
    bot.send_message(message.chat.id, "Comenzi disponibile:\n/start - pentru a porni botul\n/help - pentru ajutor")
    
@bot.message_handler(commands=['info', 'инфориация', 'инфо'])
def info_command(message):
    bot.send_message(message.chat.id, "Aici gasiti informatii despre bot.")
    
@bot.message_handler()
def info(message):
    raspunsuri = {
        "hello": lambda m:  bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}'),
        "id" : lambda m: bot.reply_to(message, f"ID=ul tau este: {message.from_user.id}"),
        "hi":lambda m: bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}')
    }
    mess = message.text.lower()
    if mess in raspunsuri:
        raspunsuri[mess](message)
    
    
    
    
    
      
    
    
bot.polling(none_stop=True)