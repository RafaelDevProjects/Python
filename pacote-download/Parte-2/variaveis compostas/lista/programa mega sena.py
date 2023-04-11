from random import randint
from time import sleep
jogos=[]
list=[]
print('--'*20)
print(F'{"JOGA NA MEGA SENA":^40}')
print('--'*20)
sorteio=[]
quant= int(input('quantos jogos da mega sena quer sortear?'))
print('=-'*5,F'SORTEANDO {quant} JOGOS','-='*5)
tot=1
while tot <= quant:
    cont=0
    while True:
        num = randint(1,60)
        if num not in list:
            list.append(num)
            cont+=1
        if cont >= 6:
            break
    list.sort()
    jogos.append(list[:])
    list.clear()
    tot += 1
for e,c in enumerate(jogos):
    print(f'jogo {e+1}: {c}')
    sleep(1)

