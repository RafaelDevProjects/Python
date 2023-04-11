dados=list()
pessoas=list()
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        maior=menor=dados[1]
    else:
        if dados[1] > maior:
            maior=dados[1]
        if dados[1] < menor:
            menor=dados[1]
    pessoas.append(dados[:])
    dados.clear()
    print(20*'=')
    r = str(input('Deseja continuar[S/N] ? ')).strip()[0]
    print(20 * '=')
    if r in 'nN':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso foi {maior} Kg, o peso de',end= ' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{[p[0]]}',end=' ')
print()
print(f'O menor peso foi {menor} Kg, o peso de',end= ' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{[p[0]]}',end= ' ')
print()

