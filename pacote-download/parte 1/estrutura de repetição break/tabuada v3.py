from time import sleep
print(10*'-','\033[0;32;40mProgarama de Tabuada\033[m','-'*10)
cont=0
while True:
    print('=' * 40)
    num=int(input('Quer ver a tabuada de qual valor?'))
    print('='*40)
    if num < 0:
        break
    for c in range (1,11):
        print(f'{c} X {num} = {c*num}')
print('FINALIZANDO O PROGRAMA...')
sleep(2)
print('\033[0;32;40mFINALIZADO\033[m')



