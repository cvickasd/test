from telebot import TeleBot
bot = TeleBot('6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q')
lst={}


@bot.message_handler(commands=['start'])
def start(message):
    lst[message.from_user.first_name]='шоколадка'
    bot.send_message(message.chat.id, lst)

bot.polling()
