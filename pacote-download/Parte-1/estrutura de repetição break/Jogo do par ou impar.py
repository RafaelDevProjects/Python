from random import randint
from time import sleep
print('-'*20,'\033[0;32;40mJOGO PAR OU IMPAR\033[0m','-'*20)
soma=0
cont=0
v=0
while True:
    jogada = ' '
    while jogada not in 'PI':
        jogada = str(input('Escolha!! PAR ou IMPAR:')).upper().strip()[0]
    jogador = int(input('Faça sua jogada! Digite um numero:'))
    print('~' * 50)
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'O computador jogou \033[0;32;40m{computador}\033[m e você jogou \033[0;32;40m{jogador}\033[m. Dando um total de \033[0;32;40m{soma}\033[m')
    print('~' * 50)
    sleep(1)
    print('DEU PAR' if soma % 2  == 0 else 'DEU IMPAR')
    if jogada== 'P':
        if soma % 2 ==0:
            v+=1
            print('Você \033[0;32;40mVENCEU!!!\033[m')
            print('~' * 50)
        else:
            print('Você \033[0;32;40mPERDEU!!!\033[m')
            print('~' * 50)
            break
    elif jogada == 'I':
        if soma % 2 == 1:
            print('Você \033[0;32;40mVENCEU!!!\033[m')
            print('~' * 50)
            v += 1
        else:
            print('Você \033[0;32;40mPERDEU!!!\033[m')
            print('~' * 50)
            break
    print('Vamos jogar novamente...')
print(f'FIM DE JOGO. Você conseguiu ganhar \033[0;32;40m{v}\033[m vezes do computador')




