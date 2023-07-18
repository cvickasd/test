from telebot import TeleBot
from random import choice
import os
import json
TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['save'])
def save(message):
    if os.path.exists('score.json'):
        with open('score.json', 'r', encoding='utf-8') as f:
            score = json.load(f)
    else:
        score = {}
    global group_id
    points = 123456789
    group_id = message.chat.id
    user_name = message.from_user.first_name
    score[user_name]=[points,group_id]
    with open('score.json', 'w', encoding='utf-8') as f:
        json.dump(score,f)
    bot.send_message(message.chat.id, text='Прогресс сохранён') 
    bot.send_message(message.chat.id, score[message.from_user.first_name])
    bot.send_message(message.chat.id, score[message.from_user.first_name][1])
if __name__ == '__main__':
    bot.polling(none_stop=True)