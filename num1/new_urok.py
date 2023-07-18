from telebot import TeleBot, types
import json

TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)

game = False
indx = 0
points = 0

with open('victorina.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_next_question(data,indx):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(4):
        btn = types.KeyboardButton(data[indx]['вариант'][i])
        markup.add(btn)
    markup.add(types.KeyboardButton('Выход'))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['quizz'])
def quizz(message):
    global game, indx
    game = True
    markup = get_next_question(data,indx)
    bot.send_message(message.chat.id, text=data[indx]['вопрос'], reply_markup=markup)
@bot.message_handler()
def all(message):
    global game,indx,points
    if game:
        if message.text == data[indx]['ответ']:
            bot.send_message(message.chat.id,'Правильно')
            points += 1
        elif message.text == 'Выход':
            bot.send_message(message.chat.id,'Пока')
            game = False
            return
        else:
            markup = get_next_question(data,indx)
            bot.send_message(message.chat.id, f'Неправильно! Правильный ответ-{data[indx]["ответ"]}')
        indx +=1 
        markup = get_next_question(data,indx)
        bot.send_message(message.chat.id, text=data[indx]['вопрос'], reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)