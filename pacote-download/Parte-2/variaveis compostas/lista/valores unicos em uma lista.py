valores=[]
while True:
    n=int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado! não irei adicionar...')
    print('Valor adicionado...')
    r = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]
    if r in 'Nn':
        break
valores.sort()
print(30*'-=')
print(f'Os numeros adicionados em ordem crescente são {valores}')