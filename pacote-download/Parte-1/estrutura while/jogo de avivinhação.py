from random import randint
from time import sleep
computador=randint(0, 10)

print('-==-'*20)
print('Olá, meu nome é computador, muito prazer!!!')
print('-==-'*20)
print('Vou pensar em m numero de 0 a 10, tente acertar e ganhar de mim...')
print('Pensando...')
sleep(3)

palpites=0
acertou = False
while not acertou:
    palpites+=1
    jogador = int(input('Seu palpite: '))
    if jogador == computador:
        acertou = True
    if jogador < computador:
        print('Mais...')
    elif jogador > computador:
        print('Menos..')
print('Acertou !!!')
print('Foram precisos {} palpites para chegar a resposta. Parabéns!'.format(palpites))