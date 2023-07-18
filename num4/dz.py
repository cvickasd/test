from telebot import types, TeleBot
from random import randint
from time import time

numbers = ['один','два','три','четыре','пять','шесть','семь','восемь','девять','десять']
bot = TeleBot('6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q')

random_number1 = randint(1,5)
random_number2 = randint(1,5)
total_amount =  random_number1 + random_number2

with open('C:/python_file/num4/bad_words.txt', 'r', encoding='utf-8') as f:
    data = f.read().split(' ')


def has_bad_words(message):
    global a
    words = message.text.lower().split(' ')
    for word in words:
        if word in data:
            if word in ('чо','чё','че'):
                print('asdasd')
                a=True
            return True
    return False


def is_group(message):
    return message.chat.type in ('group', 'supergroup') 


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
    has_bad_words(message)
    keys=[]
    for indx, number in enumerate(numbers):
        keys.append(types.InlineKeyboardButton(text=number, callback_data=indx+1))
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(*keys)

    bot.send_message(message.chat.id, text=f'Сколько будет {random_number1} + {random_number2}', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global total_amount
    if int(call.data) == total_amount:
        bot.send_message(chat_id=call.message.chat.id, text="Правильно")
    if int(call.data) != total_amount:
        bot.restrict_chat_member(chat_id=call.message.chat.id, user_id=call.from_user.id, until_date=time()+60)
        bot.send_message(chat_id=call.message.chat.id, text="Не Правильно!!!")


bot.polling(none_stop=True)
