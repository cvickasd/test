from telebot import TeleBot, types
import random

TOKEN = '6149703984:AAERkO3wEQOxCDSO30sm-mYORbQL6TBox_Q'
bot = TeleBot(TOKEN)
number = 0
nbr = 0

rols = ['Мирный']
player1 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер1', 'Очки': 0}
player2 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер2', 'Очки': 0}
player3 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер3', 'Очки': 0}
player4 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер4', 'Очки': 0}
player5 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер5', 'Очки': 0}
players = [player1, player2, player3, player4, player5]

@bot.message_handler(commands=['роль'])
def vidat_rols(message):
	for i in players:
		global nbr
		if nbr == 4:
			bot.send_message(message.chat.id, i['Имя'])
			bot.send_message(message.chat.id, f'Ваша роль: Мафия')
			break			
		rol = random.choice(rols)
		bot.send_message(message.chat.id, i['Имя'])
		bot.send_message(message.chat.id, f'Ваша роль:{rol}')
		i['Роль'] = rol
		if rol == 'Мафия':
			rols.pop(1)
		elif rol == 'Мирный':
			nbr +=1
	bot.send_message(message.chat.id, nbr) 
mafia = None
for i in players:
	if i['Роль'] == 'Мафия':
		mafia = i
def kill(name):
	name['Состояние'] == False
@bot.message_handler(commands=['убить'])
def kil(message):
	killer = message.text.split(' ')[1]
	for i in players:
		if i['Имя'] == killer:
			kill(i)  
			bot.send_message(message.chat.id, 'Убит:', i['Имя'])
player1_golos = None
@bot.message_handler(commands=['голос1'])
def golos1(message):
	player1_golos = message.text.split(' ')[1]
player2_golos = None
@bot.message_handler(commands=['голос2'])
def golos2(message):
	player1_golos = message.text.split(' ')[1]
player3_golos = None
@bot.message_handler(commands=['голос3'])
def golos3(message):
	player1_golos = message.text.split(' ')[1]
player4_golos = None
@bot.message_handler(commands=['голос4'])
def golos4(message):
	player1_golos = message.text.split(' ')[1]
player5_golos = None
@bot.message_handler(commands=['голос5'])
def golos5(message):
	player1_golos = message.text.split(' ')[1]
	number +=1

if number >= 1:
	players_goloss = [player1_golos, player2_golos, player3_golos,
	 	player4_golos, player5_golos]
	for player in players:
		for golos in players_goloss:
			if player['Имя'] == golos:
				player['Очки'] += 1
	max_value = max(player1['Очки'], player2['Очки'], player3['Очки'], player4['Очки'], player5['Очки'])
	max_var_name = None
	if max_value == player1['Очки']:
	    max_var_name = player1
	elif max_value == player2['Очки']:
	    max_var_name = player2
	elif max_value == player3['Очки']:
	    max_var_name = player3
	elif max_value == player4['Очки']:
	    max_var_name = player4
	elif max_value == player5['Очки']:
	    max_var_name = player5

	kill(max_var_name)
	@bot.message_handler(commands=['death'])
	def death(message):
		for i in players:
			if i['Состояние'] == False:
				bot.send_message(message.chat.id, i)
	
	number = 0



if __name__ == '__main__':
    bot.polling(none_stop=True)