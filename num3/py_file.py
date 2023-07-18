from telebot import TeleBot, types
import json
import random as rn

TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)

game = False
indx = rn.randint(0,2)
points = 0

with open('json_file.json', 'r', encoding='utf-8') as f:
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
        try:
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
            # if len(data) < indx:
            #     markup = get_next_question(data,indx)
            if 'image' in data[indx]:
                img = open(data[indx]['image'], 'rb')
                bot.send_photo(message.chat.id,img)
                img.close()

            markup = get_next_question(data,indx)
            bot.send_message(message.chat.id, text=data[indx]['вопрос'], reply_markup=markup)
        except:
            indx = rn.randint(0,2)

if __name__ == '__main__':
    bot.polling(none_stop=True)