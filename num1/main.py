
from telebot import TeleBot
from random import choice
from random import randint

# Уникальный токе который получаем от @BotFather
TOKEN = '5870120367:AAFxnWFhWGLa0Dol6AyRQ64VkIVdnRYYq90'
bot = TeleBot(TOKEN)

shutky = [
    '— Санек, ты странный, конечно.\n— Почему это я странный?\n— Живешь возле кладбища, а к чаю ничего нет.',
    'Похоронил пацанчик друга своего, захотел с горя покурить, а сигарет нет. Приходит в табачный магазин, а ему с порога:\n— Кента нет.',
    'Вена, 1824 год.\n— Ну что, пойдем завтра в оперу?\n— Да, надо бы. Бетховен сам себя не послушает.'
]

@bot.message_handler(commands=['rps'])
def rps(message):
    lst = ['камень', 'ножницы', 'бумага']
    a = choice(lst)
    bot.send_message(message.chat.id, a)
    msg = message.text.split(' ')[1]
    result = {
        'камень': {'камень': 'Ничья!', 'ножницы': 'Ты выиграл!', 'бумага': 'Ты проиграл!'},
        'ножницы': {'камень': 'Ты проиграл!', 'ножницы': 'Ничья!', 'бумага': 'Ты выиграл!'},
        'бумага': {'камень': 'Ты выиграл!', 'ножницы': 'Ты проиграл!', 'бумага': 'Ничья!'}
    }
    bot.send_message(message.chat.id, result[msg][a])

@bot.message_handler(commands=['random'])
def random(message):
    soob = message.text.split(' ')
    texxt = randint(int(soob[1]),int(soob[2]))
    bot.send_message(message.chat.id, texxt)

@bot.message_handler(commands=['sum'])
def sum(message):
    vlos = message.text.split(' ')
    for i in vlos:
        try:
            sumn = int(vlos[1]) + int(i)
        except:
            pass
    bot.send_message(message.chat.id, sumn)

@bot.message_handler(commands=['umno'])
def umno(message):
    asd = message.text.split(' ')
    um = float(asd[1]) * float(asd[2])
    bot.send_message(message.chat.id, um)

@bot.message_handler(commands=['del'])
def sum(message):
    o = message.text.split(' ')
    j = float(o[1]) / float(o[2])
    bot.send_message(message.chat.id, j)

@bot.message_handler(commands=['vich'])
def sum(message):
    f = message.text.split(' ')
    h = float(f[1]) - float(f[2])
    bot.send_message(message.chat.id, h)

# Бот реагирует на команду /choc
@bot.message_handler(commands=['choc'])
def start(message):
    bot.send_message(message.chat.id, 'chocфыв')
# Бот реагирует на команду /loca
@bot.message_handler(commands=['loca'])
def lc(message):
    bot.send_message(message.chat.id, 'locaasd')



# Бот отвечает тем же, что написал пользователь
@bot.message_handler()
def echo(message):
    if message.text == 'шутка':
        bot.send_message(message.chat.id, choice(shutky))
        return
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
