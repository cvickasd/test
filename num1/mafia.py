import random

# players
rols = ['Мирный', 'Мафия']
player1 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер1', 'Очки': 0}
player2 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер2', 'Очки': 0}
player3 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер3', 'Очки': 0}
player4 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер4', 'Очки': 0}
player5 = {'Роль': None, 'Состояние': True, 'Имя': 'Номер5', 'Очки': 0}
players = [player1, player2, player3, player4, player5]

#who killer?
for i in players:
    rol = random.choice(rols)
    print(i['Имя'])
    print('Ваша роль:', rol)
    i['Роль'] = rol
    if rol == 'Мафия':
        rols.remove('Мафия')
mafia = None
for i in players:
    if i['Роль'] == 'Мафия':
        mafia = i

# kill
def kill(name):
    name['Состояние'] = False

killer = input('Кого вы убьёте?')
for i in players:
    if i['Имя'] == killer:
        kill(i)

# голосование
player1_golos = input('За кого вы голосуете?')
player2_golos = input('За кого вы голосуете?')
player3_golos = input('За кого вы голосуете?')
player4_golos = input('За кого вы голосуете?')
player5_golos = input('За кого вы голосуете?')
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

for i in players:
    if i['Состояние'] == False:
        print(i)
