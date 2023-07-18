from telebot import TeleBot, types
import requests
import wikipedia 

wikipedia.set_lang('ru')

TOKEN = '5870120367:AAFxnWFhWGLa0Dol6AyRQ64VkIVdnRYYq90'
bot = TeleBot(TOKEN)

@bot.callback_query_handler(func = lambda call: call.data)
def answer(call):
    page = wikipedia.page(call.data)
    bot.send_message(call.message.chat.id, text=page.title)
    bot.send_message(call.message.chat.id, text=page.summary)
    bot.send_message(call.message.chat.id, text=page.url)

@bot.message_handler(commands=['wiki'])
def start(message):
    query = ' '.join(message.text.split(' ')[1:])
    results = wikipedia.search(query)
    markup = types.InlineKeyboardMarkup()
    for result in results:
        btn = types.InlineKeyboardButton(result, callback_data=result)
        markup.add(btn)
    bot.send_message(message.chat.id, 'Нашлось:', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

def get_duck_url():
    url = 'https://random-d.uk/api/random'
    response = requests.get(url)
    data = response.json()
    return data['url']

@bot.message_handler(commands=['duck'])
def start(message):
    url = get_duck_url()
    bot.send_message(message.chat.id, url)

def get_fox_url():
    url = 'https://randomfox.ca/floof'
    response = requests.get(url)
    data = response.json()
    return data['image']

@bot.message_handler(commands=['fox'])
def start(message):
    url1 = get_fox_url()
    bot.send_message(message.chat.id, url1)

if __name__ == '__main__':
    bot.polling(none_stop=True)

