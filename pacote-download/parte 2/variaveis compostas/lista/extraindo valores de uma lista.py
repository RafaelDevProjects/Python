lista=[]
while True:
    lista.append(int(input('Digite um valor a lista: ')))
    r = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
lista.sort(reverse=True)
print(f'A quantidade de valores na lista é de {len(lista)} números')
print(f'A lista em ordem decresente : {lista}')
if 5 not in lista:
    print('O valor 5 não foi achado na lista!')
else:
    print('O valor 5 esta na lista!')


