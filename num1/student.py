#1игроки
import random as rnd
#4игроки
player_one= {'роль':None, 'живой/неживой': True, 'имя': '1'}
player_two= {'роль':None, 'живой/неживой': True,'имя': '2'}
player_three= {'роль':None, 'живой/неживой': True,'имя': '3'}
player_four= {'роль':None, 'живой/неживой': True,'имя': '4'}
player_five= {'роль':None, 'живой/неживой': True,'имя': '5'}

players = [player_one,player_two,player_three,player_four,player_five]

#2раздача ролей
rols = ['мирный','мафия']

for i in players:
    rol = rnd.choice(rols)
    i['роль'] = rol
    if rol == 'мафия':
        rols.remove('мафия')
#3роль #7узнаем кто мафия
mafia = None
for i in players:
    print(i)
    if i['роль'] == 'мафия':
        mafia = i 
#5 функция kill
def kill(name):
    name['живой/неживой'] = False
#6 все засыпают мафия просыпается
mir_liva = True
mafia_lifva = True
while mir_liva == True and mafia_lifva == True:
    print('Всем спать!!! Мафия просыпается')
    #8 мафия пускает первую кровь
    # здесь должна быть функция где спрашивают именно мафия но я хз как сделать в терменале
    kill_name = int(input('Кто должен сдохнуть?1,2,3,4,5'))
    kill_name = players[(kill_name-1)]
    vse_mirnie_lifa = 0
    kill(kill_name)
    #9написать кто умер
    # print('Умер:', kill_name['имя'])
    for i in players:
        if i['роль'] == 'мирный':
            if i['живой/неживой'] == True:
                vse_mirnie_lifa += 1
            if vse_mirnie_lifa >= 2:
                mir_liva = True

    #голосование
    def plus_golos(za):
        

    def golosovanie():
        one_people = 0
        two_people = 0
        three_people= 0
        four_people= 0
        five_people= 0
        pepoles = [one_people,two_people,three_people,four_people,five_people]
        goloss = [one_golos,two_golos,three_golos,four_golos,five_golos]
        one_golos = input('За кого ты?1,2,3,4,5')
        two_golos = input('За кого ты?1,2,3,4,5')
        three_golos = input('За кого ты?1,2,3,4,5')
        four_golos = input('За кого ты?1,2,3,4,5')
        five_golos = input('За кого ты?1,2,3,4,5')
            
        plus_golos(pepoles[one_golos-1])
        plus_golos(pepoles[two_golos-1])
        plus_golos(pepoles[three_golos-1])
        plus_golos(pepoles[four_golos-1])
        plus_golos(pepoles[five_golos-1])
    golosovanie()
    if mafia['живой/неживой'] == True:
        mafia_lifva == True
    # print(players)
if mafia_lifva == False:
    print('Мирные победили')
else:
    print('Мафия победила') 