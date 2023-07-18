from telebot import TeleBot, types
import requests
import wikipedia 

wikipedia.set_lang('ru')

TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)

def get_dog_url():
    # url = 'https://random.dog'
    # response = requests.get(url)
    # data = response.json()
    # return data['url']
    url = 'https://random.dog/woof.json'
    response = requests.get(url)
    data = response.json()
    return data['url']
    # bot.send_photo(message.chat_id, photo=photo_url)

@bot.message_handler(commands=['dog'])
def start(message):
    url = get_dog_url()
    bot.send_message(message.chat.id, url)

if __name__ == '__main__':
    bot.polling(none_stop=True)