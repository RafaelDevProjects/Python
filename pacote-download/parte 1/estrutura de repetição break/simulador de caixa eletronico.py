print('='*30)
print(('      \033[0;32;40m BANCO OFICIAL \033[m'))
print('='*30)
valor=int(input('Quanto quer sacar? R$'))
total=valor
ced=50
totced=0
while True:
    if total >= ced:
        total-=ced
        totced+=1
    else:
        print(f'Total de {totced} cedulas de R$ {ced} ')
        if ced == 50:
            ced=20
        elif ced == 20:
            ced=10
        elif ced == 10:
            ced=1
        totced=0
        if total ==0:
            break
print('='*30)
print('Volte sempre ao banco oficial')

