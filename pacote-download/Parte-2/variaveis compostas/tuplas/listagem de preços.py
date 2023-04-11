print(47*'-')
print(f'\033[0;32m{"LISTAGEM DE PREÇOS":^47}\033[m')
print(47*'-')
listagem=('Caneta', 2.00,
          'Borracha', 5.00,
          'Lapisera', 8.50,
          'Caderno', 20.99,
          'Estogo', 30.50,
          'livro didatico', 10.99,
          'Teclado', 30.60,
          'Folha sufite', 10.50,
          'Mouse', 100.00)
for item in range (0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<38}', end= '')
    if item % 2 == 1:
        print(f'R${listagem[item]:>7.2f}')
print(47*'-')
