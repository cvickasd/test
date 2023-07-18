from telebot import TeleBot
from random import choice	

bot = TeleBot('6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q')

false_mesg = ''

with open("russians_words.txt", 'r', encoding='utf-8') as f:
	data=f.read().split('\n')


using_words = []# usin_words = список
using_wording = ''# usin_wording = ''
en_wd = 'сумма' # en_wd = 'сумма'  (пишем сумма чтобы первое слово была на 'a' и не было гемороя)


@bot.message_handler(commands=['play'])
def play(msg):
    random_word(msg) 


@bot.message_handler(commands=['us'])
def play(msg):
    bot.send_message(msg.chat.id, using_wording)


@bot.message_handler(commands=['en'])
def play(msg):
    bot.send_message(msg.chat.id, en_wd)


@bot.message_handler(commands=['add'])
def add(msg):
    if msg.text.lower().split(" ")[1] not in data:
        with open("russians_words.txt", "a", encoding='utf-8') as myfile:
            myfile.write(f'\n{msg.text.lower().split(" ")[1]}')
        bot.send_message(msg.chat.id, 'Успешно добавлено!')
    else:
        bot.send_message(msg.chat.id, 'Такое слово уже есть!')
def random_word(msg):# добавить функцию random word, 
    global using_wording, using_words
    using_wording = choice(data)# rn_word = должна выбирать случайное слово из data
    while using_wording[0] != en_wd[prov(en_wd)] or using_wording in using_words: using_wording = choice(data)# повтарять если  НЕ первая буква равна последней букве слова en_wd и этого слова нету в usin_words
	 
    using_words.append(using_wording) # добавить в using_wirds rn_word
     # using_wording = rn_word
    mesg = bot.send_message(msg.chat.id, using_wording) # print(using_wording)
    bot.register_next_step_handler(mesg, enemy) # enemy(input('Ваша очередь: '))


def enemy(msg): # добавить функцию enemy принимающие message(то есть сообщение)
    global en_wd, using_words
    # if msg.text.lower()[0] != en_wd[(len(en_wd)-1)] or msg.text.lower() not in data or msg.text.lower() in using_words: # проверить, если текст в собщении равен последней букве нашего слова и его ещё нету в using_words
    #     random_word(msg) # иначе попросить снова написать слово
    #     return
    if msg.text.lower()[0] == '/':
        bot.send_message(msg.chat.id, 'Прошу напишите снова команду, игра закончилась')
        return 
    if msg.text.lower() == '/stop':
        bot.send_message(msg.chat.id, 'Игра закончилась')
        return 
    if msg.text.lower() in using_words:
        mesg = bot.send_message(msg.chat.id, 'Вы или я уже писали такое слово((. Прошу напишите другое слово')
        bot.register_next_step_handler(mesg, enemy)
        return
    if msg.text.lower() not in data:
        mesg = bot.send_message(msg.chat.id, 'У нас нет такого слова((. Прошу напишите другое слово')
        bot.register_next_step_handler(mesg, enemy)
        return
    if msg.text.lower()[0] != using_wording[prov(using_wording)]:
        mesg = bot.send_message(msg.chat.id, 'Не правильная буква((. Прошу напишите другое слово')
        bot.register_next_step_handler(mesg, enemy)
        return
    if msg.text.lower()[0] == using_wording[prov(using_wording)] or msg.text.lower() in data or msg.text.lower() not in using_words: 
        using_words.append(msg.text.lower()) # добавить слово в using_words
        en_wd = msg.text.lower() # en_wd = сообщение.text
        random_word(msg)


def prov(word):
    i = -1
    while word[i] in ('й', 'ь', 'ъ', 'ы'):
        i-=1
    return i






bot.polling()
