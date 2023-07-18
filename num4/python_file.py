from telebot import TeleBot
from random import choice
import time


TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)
game=False
game2=False
players={}
rols=[]
players_name=[]
count_players=0
number=0
name=None
yes=False
group_id=None
names=[]


@bot.message_handler(commands=['game'])
def game(message):
    global game, game2, group_id
    bot.send_message(message.chat.id, 'У вас 30 сек чтобы зарегаться')
    timer = 30
    start_time = time.time()
    sent_message = bot.send_message(message.chat.id, int(time.time() - start_time))
    message_id = sent_message.message_id
    while time.time() - start_time < timer:
        game2=True
        time.sleep(1)  # увеличиваем время задержки
        number = int(time.time() - start_time)
        bot.edit_message_text(chat_id=message.chat.id, message_id=message_id, text=str(number))
    bot.send_message(message.chat.id, 'Время вышло!')
    game=True
    group_id = message.chat.id
    bot.send_message(message.chat.id, 'Сейчас выберут случайного игрока и всем будет выслоно его роль(конечно кроме самого игрока)')


@bot.message_handler(commands=['i_play'])
def playeeeeer(message):
    global game2, players, rols,players_name, count_players
    if game2:
        global players,count_players,points_players
        if message.from_user.first_name in players:
            bot.send_message(message.chat.id, 'Куда лезешь?')
        elif message.from_user.first_name not in players and len(players_name) < 5:
            count_players+=1
            rol = message.text.split(' ')
            rols.append(rol)
            players_name.append(message.from_user.first_name)
            players[message.from_user.first_name]={'ID':message.from_user.id, 'Роль':None}
            bot.send_message(group_id, f'{message.from_user.first_name} вы зарегестрированы')


@bot.message_handler(commands=['play'])
def play(message):
    global name, number
    if number == 0:
        new_rols = []
        for i in players:
            new_rols = []
            rol = choice(rols)
            if rol not in new_rols:
                players[i]['Роль']=(rol)
        number +=1
    name = choice(players_name)
    names.append(name)
    bot.send_message(group_id,f'{name} вы должны понять кто вы')
    for i in players:
        if i != players[name]['ID']:
            bot.send_message(players[i]['ID'], f'Вы должны НАМЕКНУТЬ человеку роль, вот его ник: {name}')
    global yes
    yes=True


def play_game(message):
    should_restart = True
    while should_restart:
        should_restart = False
        name = choice(players)
        if name not in names:
            names.append(name)
            bot.send_message(group_id,f'{name} вы должны понять кто вы')
            for i in players:
                if i != players[name]['ID']:
                    bot.send_message(players[i]['ID'], f'Вы должны НАМЕКНУТЬ человеку роль, вот его ник: {name}')
        elif name in names:
            should_restart = True
            break

@bot.message_handler()
def plaing_game(message):
    if message.text == name and players[name]['ID']==message.from_user.id:
        bot.send_message(message.chat.id, 'Вы Угадали!')
        play_game(message)
    elif message.text == name and players[name]['ID'] != message.from_user.id and message.chat.id == group_id:
        bot.delete_message(chat_id=group_id, message_id=message.reply_to_message.message_id)
        bot.send_message(group_id, 'Нельзя напрямую говорить роль')

        
bot.polling()
