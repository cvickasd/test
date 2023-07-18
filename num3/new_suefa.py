from telebot import TeleBot, types
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)
suefa_lst = ['Камень', 'Бумага', 'Ножницы']
game1 = False
game2 = False
players = {
    'player1': {
        'name':None,
        'ход':None},
    'player2': {
        'name':None,
        'ход':None}
}
group = None
ls1 = None
ls2 = None
@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Камень')
    markup.add('Бумага')
    markup.add('Ножницы')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=markup)

@bot.message_handler(commands=['start_game'])
def msg(message):
    global group
    group = message.from_user.id
@bot.message_handler(commands=['result'])
def result(message):
    global suefa_lst,players, game1, game2
    if game1 == True and game2 == True:
        win_defeat = {
        "Камень":{"Камень":'Ничья',"Бумага":players['player2']['name'],"Ножницы":players['player1']['name']},
        "Бумага":{"Бумага":'Ничья',"Ножницы":players['player2']['name'],"Камень":players['player1']['name']},
        "Ножницы":{"Ножницы":'Ничья',"Камень":players['player2']['name'],"Бумага":players['player1']['name']}
       }
        bot.send_message(message.chat.group, 'Победил: '+win_defeat[players['player1']['ход']][players['player2']['ход']])
        players['player1']['name'] = None
        players['player1']['ход'] = None
        players['player2']['name'] = None
        players['player2']['ход'] = None
        game1 = False
        game2 = False
@bot.message_handler()
def gaming(message):
    global suefa_lst,players, game1, game2, ls
    if message.text in suefa_lst:
        if players['player1']['name'] == None:
            ls1 = int(message.from_user.id)
            players['player1']['name'] = message.from_user.first_name
            bot.send_message(message.chat.ls1, 'Вы играете: ' + players['player1']['name'])
            players['player1']['ход'] = message.text
            game1 = True
        elif players['player2']['name'] == None:
            ls2 = int(message.from_user.id)
            players['player2']['name'] = message.from_user.first_name
            bot.send_message(message.chat.ls2, 'Вы играете: ' + players['player2']['name'])
            players['player2']['ход'] = message.text
            game2 = True

if __name__ == '__main__':
    bot.polling(none_stop=True)