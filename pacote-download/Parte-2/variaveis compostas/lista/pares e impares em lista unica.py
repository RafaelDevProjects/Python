lista=list()
impares=list()
pares=list()
for c in range (1,8):
    num=int(input(f'Digite o {c}o. valor:'))
    if num % 2 == 0 :
        pares.append(num)
    else:
        impares.append(num)
lista.append(impares)
lista.append(pares)
lista[1].sort()
lista[0].sort()
print(20*'-=')
print(f'Os numeros pares são {lista[1]}')
print(f'Os numeros impares são {lista[0]}')
