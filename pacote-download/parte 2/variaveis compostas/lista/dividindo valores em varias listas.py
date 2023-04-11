lista=[]
listaimp=[]
listapar=[]
while True:
    lista.append(int(input('Digite um valor para a lista:')))
    r = str(input('Deseja continuar [S/N]? ')).strip()[0]
    if r in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimp.append(c)
print(30*'-=')
print(f'A sua lista foi {lista}')
print(f'Os numeros impares foram {listaimp}')
print(f'Os numeros pares foram {listapar}')
