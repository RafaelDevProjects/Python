from random import randint
tupla= (randint(1,10), randint(1,10), randint(1,10) , randint(1,10) , randint(1,10))
print(f'Os valores sortiados foram:', end= ' ')
for c in tupla:
    print(f'{c} ', end= '')
print('\n','-='*20)
print(f'\nO maior numero sorteado foi {max(tupla)}')
print(f'O menor numero sorteado foi {min(tupla)}')
