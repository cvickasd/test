from telebot import TeleBot
from time import time

TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)
# bad_words=['пидор','чё','чо','че','хуй']
a=None
with open('C:/python_file/num4/bad_words.txt', 'r', encoding='utf-8') as f:
    bad_words = f.read().split(' ')

def is_group(message):
    return message.chat.type in ('group', 'supergroup') 


def has_bad_words(message):
    global a
    words = message.text.lower().split(' ')
    for word in words:
        if word in bad_words:
            if word in ('чо','чё','че'):
                print('asdasd')
                a=True
            return True
    return False


@bot.message_handler(func=lambda message: has_bad_words(message) and is_group(message))
def moderate(message):
    bot.restrict_chat_member(
        message.chat.id,
        message.from_user.id,
        until_date=time()+60)
    if a == True:
        bot.send_message(message.chat.id, 'через плечо')
        return
    bot.send_message(message.chat.id, 'уважаю')
    bot.delete_message(message.chat.id, message_id=message.message_id)


@bot.message_handler(func=lambda message: message.entities is not None and is_group(message))
def start(message):
    for entity in message.entities:
        if entity.type in ['url', 'text_link']:
            bot.delete_message(message.chat.id, message_id=message.message_id)


bot.polling(none_stop=True)