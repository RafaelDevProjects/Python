from random import randint
from time import sleep
from operator import itemgetter #pega um item especifico em uma chave especifica
jogadas={}
jogadas['jogador1']=randint(1,6)
jogadas['jogador2']=randint(1,6)
jogadas['jogador3']=randint(1,6)
jogadas['jogador4']=randint(1,6)
ranking=dict()
print('-='*3,'DADO JOGADO','-='*3)
for k, v in jogadas.items():
    print(f'{k} tirou = {v}')
    sleep(0.5)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse= True)
print('='*6,'RANKING','='*6)
for k, v in enumerate (ranking):
    print(f'{k+1} lugar: {v[0]} com {v[1]}')
    sleep(0.5)
    