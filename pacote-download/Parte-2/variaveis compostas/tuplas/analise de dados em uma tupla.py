
n=int(input('Digite um valor:'))
c=int(input('Digite  mais um valor:'))
d=int(input('Digite outro valor:'))
e=int(input('Digite um quarto valor:'))
numeros=(n,c,d,e)
print(f'Você digitou os valores{numeros}')
print(f'O numero 9 foi usado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 foi usado pela primeira vez na {numeros.index(3) + 1} posição')
else:
    print('Você não digitou o valor 3')
print('Os valores parares digitados foram:',end= ' ')
for x in numeros:
    if x % 2==0:
        print(x, end = ' ')
