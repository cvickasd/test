from telebot import TeleBot
from random import choice
import os
import json
TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)
game = False
used_words = []
letter = ''
points = 0


with open('cities.txt', 'r', encoding='utf-8') as f:
    data = [line.strip().lower() for line in f.readlines()]


def select_letter(word):
    i = -1
    while word[i] in ('ы','ь','ъ','й'):
        i-=1
    return word[i]


@bot.message_handler(commands=['save'])
def save(message):
    if os.path.exists('score.json'):
        with open('score.json', 'r', encoding='utf-8') as f:
            score = json.load(f)
    else:
        score = {}
    global player_id
    player_id = message.chat.id
    bot.send_message(message.chat.id, player_id)
    user_name = message.from_user.first_name
    score[user_name]=[points,player_id]
    with open('score.json', 'w', encoding='utf-8') as f:
        json.dump(score,f)
    bot.send_message(message.chat.id, text='Прогресс сохранён') 
    bot.send_message(message.chat.id, score)
@bot.message_handler(commands=['print_points'])
def print_points(message):
    with open('score.json', 'r', encoding='utf-8') as f:
        pointss = json.load(f)
    if message.from_user.first_name in pointss:
        bot.send_message(message.chat.id, pointss[message.from_user.first_name][0])


@bot.message_handler(commands=['gorod'])
def gorod(message):
    global game, letter
    game=True
    city = choice(data)
    letter = select_letter(city)
    bot.send_message(message.chat.id, city)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler()
def ddfd(message):
    global game,used_words, letter, points
    if game:
        if message.text.lower() in used_words:
            bot.send_message(message.chat.id, 'Город уже назывался')
            return
        if message.text.lower()[0] != letter:
            bot.send_message(message.chat.id, 'Не та буква)')
            return 
        if message.text.lower() in data:
            points+=1
            letter = select_letter(message.text.lower())
            used_words.append(message.text.lower())
            for city in data:
                if city[0] == letter and city not in used_words:
                    letter = select_letter(city)
                    bot.send_message(message.chat.id, city)
                    used_words.append(city)
                    return 
            bot.send_message(message.chat.id, 'Я проиграл')
            game = False
            return
        bot.send_message(message.chat.id, 'НЕТУ такого города')



if __name__ == '__main__':
    bot.polling(none_stop=True)