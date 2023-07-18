from telebot import TeleBot
from random import choice
import json
import time

TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)
rols = ['мафия','мирный(лох)']
players = {}
points_players = {}
count_players=0
day =None
night =None
game=False
game2=False
max_count_players=0
group_id=None


@bot.message_handler(commands=['info'])
def print_inof(message):
    bot.send_message(message.chat.id, 'Косамнда /play начинает игру и вы можете зарегаться\nКосамнда /i_play надо писать в лс боту чтобы получить роль\nКосамнда /kill имя игрока писать в лс если щас ночь\nКосамнда /за имя игрока голосование когда день')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler(commands=['play'])
def play(message):
    global count_players,night, day, game, game2, group_id
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
    game2=False
    night=True  
    day=False
    count_players=0
    group_id = message.chat.id
    bot.send_message(message.chat.id, 'Все засыпают, мафия просыпается')


@bot.message_handler(commands=['i_play'])
def playeeeeer(message):
    global game2, max_count_players
    if game2:
        global players,count_players,points_players
        if message.from_user.first_name in players:
            bot.send_message(message.chat.id, 'Куда лезешь?')
        elif message.from_user.first_name not in players and max_count_players <5:
            rol = choice(rols)
            players[message.from_user.first_name]={'Роль':rol, 'Состояние':True}
            points_players[message.from_user.first_name]=0
            max_count_players+=1
            bot.send_message(message.chat.id, f'Твоя роль:{rol}')
            if rol == 'мафия':
                rols.remove('мафия')    


@bot.message_handler(commands=['kill'])
def kill(message):
    global players, night, day
    bot.send_message(message.chat.id, '1')
    if playeer and night:
        bot.send_message(message.chat.id, '2')
        if players[message.from_user.first_name]['Роль'] == 'мафия':
            msg = message.text.split(' ')[1]
            if night == True:
                players[msg]['Состояние']=False
                night=False
                day=True
                bot.send_message(message.chat.id, f'Мафия убила:{msg}')
                bot.send_message(message.chat.id, 'Ещё живые:')
                for i in players:
                    if players[i]['Состояние']==True:
                        bot.send_message(message.chat.id, i)
                playeeeeer(message)
            else:
                bot.send_message(message.chat.id, 'Нельзя днём')
        else:
            bot.send_message(message.chat.id, 'Ты не мафия))')


@bot.message_handler(commands=['за'])
def zza(message):
    if playeer():
        global points_players,count_players, players, day,night
        if day:
            msg = message.text.split(' ')[1]
            if msg in points_players and count_players<max_count_players:
                points_players[msg]+=1
                count_players+=1
            elif count_players==max_count_players:
                max_volue=0
                for i in points_players:
                    if points_players[i]>max_volue:
                        max_volue=points_players[i]
                key=list(points_players.keys())[list(points_players.values()).index(max_volue)]
                bot.send_message(message.chat.id, f'Выгнали: {key}')
                players[key]['Состояние']=False
                day = False
                night = True
                count_players=0
            playeeeeer(message)


def playeeeeer(message):
    for i in players:
        if players[i]['Состояние']==True:
            bot.send_message(group_id, i)


def playeer():
    global max_count_players
    num=0
    num2=0
    for i in players:
        if players[i]['Состояние']==True and players[i]['Роль']=='мирный':
            num+=1
    if players[i]['Роль']=='мафия':
        num2+=1
    if num!=1 and num2>=1:
        return True
    elif num<=1:
        bot.send_message(group_id, 'Мафия победила')
    elif num2==0:
        bot.send_message(group_id, 'Мирные победили')

        
if __name__ == '__main__':
    bot.polling(none_stop=True)