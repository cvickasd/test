from telebot import TeleBot
bot = TeleBot('6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q')


@bot.message_hendler(commands=['Привет!'])
def defing(message):
	bot.send_message(message.chat.id, 'чокабумбум')


bot.polling()
